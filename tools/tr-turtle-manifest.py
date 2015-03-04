#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Transform the original manifest.ttl of the Turtle test-suite
into a manifest-ldpatch.ttl adapted to LD Patch.
"""

# pylint: disable=C0103
from os.path import abspath, dirname, join
from urllib import pathname2url

from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.collection import Collection

MAIN_TESTSUITE_PATH = abspath(dirname(dirname(__file__)))
MAIN_MANIFEST_PATH = join(MAIN_TESTSUITE_PATH, "manifest.ttl")
TURTLE_TESTSUITE_PATH = join(MAIN_TESTSUITE_PATH, "turtle")
IN_MANIFEST_PATH = join(TURTLE_TESTSUITE_PATH, "manifest.ttl")
OUT_MANIFEST_PATH = join(TURTLE_TESTSUITE_PATH, "manifest-ldpatch.ttl")

MAIN_MANIFEST_IRI = URIRef("file://{}".format(pathname2url(MAIN_MANIFEST_PATH)))
IN_MANIFEST_IRI = URIRef("file://{}".format(pathname2url(IN_MANIFEST_PATH)))
OUT_MANIFEST_IRI = URIRef("file://{}".format(pathname2url(OUT_MANIFEST_PATH)))

NS = Namespace(MAIN_MANIFEST_IRI + "#")
MF = Namespace("http://www.w3.org/2001/sw/DataAccess/tests/test-manifest#")
RDFT = Namespace("http://www.w3.org/ns/rdftest#")

EMPTY_TTL = URIRef("file://{}".format(join(TURTLE_TESTSUITE_PATH, "empty.ttl")))
BASE = URIRef("http://www.w3.org/2013/TurtleTests/turtle-subm-01.ttl")

BLACKLIST = {
    "SPARQL_style_prefix", # Irrelevant: LD-Patch only accepts old-style
    "SPARQL_style_base", # @base not allowed (nor relevant) in LD-Patch
    "old_style_base", # @base not allowed (nor relevant) in LD-Patch
    "turtle-syntax-file-01", # Empty graph not allowed in LD-Patch
    "turtle-syntax-file-02", # Empty graph not allowed in LD-Patch
    "turtle-syntax-file-03", # Empty graph not allowed in LD-Patch
    "turtle-syntax-base-01", # @base not allowed (nor relevant) in LD-Patch
    "turtle-syntax-base-02", # @base not allowed (nor relevant) in LD-Patch
    "turtle-syntax-base-03", # @base not allowed (nor relevant) in LD-Patch
    "turtle-syntax-base-04", # @base not allowed (nor relevant) in LD-Patch
    "turtle-syntax-prefix-01", # Empty graph not allowed in LD-Patch
    "turtle-syntax-prefix-02", # Irrelevant: LD-Patch only accepts old-style
    "turtle-syntax-prefix-03", # Irrelevant: LD-Patch only accepts old-style
    "turtle-syntax-bad-base-01", # @base not allowed (nor relevant) in LD-Patch
    "turtle-syntax-bad-base-02", # @base not allowed (nor relevant) in LD-Patch
    "turtle-syntax-bad-base-03", # @base not allowed (nor relevant) in LD-Patch
    "turtle-syntax-bad-struct-08", # Final DOT optional in LD-Patch
    "turtle-syntax-bad-struct-11", # Final DOT optional in LD-Patch
    "turtle-subm-27", # @base not allowed (nor relevant) in LD-Patch
}


def main():
    "Generate manifest-ldpatch.ttl from manifest.ttl"
    gin = Graph()
    with open(IN_MANIFEST_PATH) as fin:
        gin.load(fin, format="turtle")
    gout = Graph()
    gout.add((OUT_MANIFEST_IRI, RDF.type, MF.Manifest))
    gout.add((OUT_MANIFEST_IRI, RDFS.comment,
              Literal("Turtle tests adapted to LD Patch")))

    ientries = Collection(gin, gin.value(IN_MANIFEST_IRI, MF.entries))
    oentries = []

    for ientry in ientries:
        if unicode(gin.value(ientry, MF.name)) in BLACKLIST:
            continue
        oentry = in2out(ientry)
        entry_name = gin.value(ientry, MF.name)
        oentries.append(oentry)
        otype = convert_entry_type(gin.value(ientry, RDF.type), entry_name)
        gout.add((oentry, RDF.type, otype))
        gout.add((oentry, MF.name, entry_name))
        gout.add((oentry, RDFT.approval, gin.value(ientry, RDFT.approval)))
        gout.add((oentry, RDFS.comment, gin.value(ientry, RDFS.comment)))

        if otype == NS.PositiveEvaluationTest:
            gout.add((oentry, MF.result, gin.value(ientry, MF.result)))

        iaction = gin.value(ientry, MF.action)
        if otype in { NS.NegativeSyntaxTest, NS.PositiveSyntaxTest }:
            gout.add((oentry, MF.action, ttl2patch(iaction)))
        else:
            oaction = BNode()
            gout.add((oentry, MF.action, oaction))
            gout.add((oaction, NS.base, BASE))
            gout.add((oaction, NS.data, EMPTY_TTL))
            gout.add((oaction, NS.patch, ttl2patch(iaction)))

    listname = BNode()
    Collection(gout, listname, oentries)
    gout.add((OUT_MANIFEST_IRI, MF.entries, listname))

    gout.namespace_manager.bind("mf", MF)
    gout.namespace_manager.bind("rdft", RDFT)
    gout.namespace_manager.bind("", NS)
    outttl = gout.serialize(format="turtle")
    outttl = (outttl.decode("utf-8") # relativize all IRIS that need to
              .replace("<" + OUT_MANIFEST_IRI, "<")
              .replace("<file://" + TURTLE_TESTSUITE_PATH + "/", "<")
              .replace("<file://" + MAIN_TESTSUITE_PATH, "<..")
             ).encode("utf-8")
    with open(OUT_MANIFEST_PATH, "w") as fout:
        fout.write(outttl)


def in2out(iri, _src=unicode(IN_MANIFEST_IRI), _dst=unicode(OUT_MANIFEST_IRI)):
    """
    Convert an IRI from the input-manifest
    into an IRI from the output manifest.
    """
    return URIRef(iri.replace(_src, _dst))


def convert_entry_type(etype, entry_name):
    "Convert a Turtle test type into an LD Patch test type."
    # exceptions
    entry_name = unicode(entry_name)
    if entry_name == "turtle-eval-bad-04":
        return NS.NegativeSyntaxTest
        # because bad IRIs are forbidden by the LD Patch syntax

    # else
    return {
        RDFT.TestTurtleEval:           NS.PositiveEvaluationTest,
        RDFT.TestTurtleNegativeEval:   NS.NegativeEvaluationTest,
        RDFT.TestTurtlePositiveSyntax: NS.PositiveSyntaxTest,
        RDFT.TestTurtleNegativeSyntax: NS.NegativeSyntaxTest,
    }[etype]

def ttl2patch(iri):
    "Convert a ttl file into an ldpatch file."
    ret = URIRef(iri.replace(".ttl", ".ldpatch"))
    ipath = unicode(iri)[7:]
    opath = unicode(ret)[7:]
    with open(opath, "w") as ofile:
        with open(ipath) as ifile:
            for line in ifile:
                if line.startswith("@prefix"):
                    ofile.write(line)
        ofile.write("Add {\n")
        with open(ipath) as ifile:
            for line in ifile:
                if not line.startswith("@prefix"):
                    ofile.write(line)
        ofile.write("} .\n")
    return ret


if __name__ == "__main__":
    main()
