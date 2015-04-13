#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Transform the original manifest.ttl of the Turtle test-suite
into a manifest-ldpatch.ttl adapted to LD Patch.
"""

# pylint: disable=C0103
import logging
from os import listdir
from os.path import abspath, dirname, join
from re import compile as regex
from urllib import pathname2url

from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.collection import Collection

LOG = logging.getLogger("gen-syntax-manifest")

TESTSUITE_PATH = dirname(dirname(abspath(__file__)))
MANIFEST_PATH = join(TESTSUITE_PATH, "manifest.ttl")
MANIFEST_SYNTAX_PATH = join(TESTSUITE_PATH, "manifest-syntax.ttl")

MANIFEST_IRI = URIRef("file://{}".format(pathname2url(MANIFEST_PATH)))
MANIFEST_SYNTAX_IRI = URIRef("file://{}".format(pathname2url(MANIFEST_SYNTAX_PATH)))

HASH = Namespace(MANIFEST_SYNTAX_IRI + "#")
FILE = Namespace(URIRef("file://{}/".format(TESTSUITE_PATH)))
NS = Namespace(MANIFEST_IRI + "#")
MF = Namespace("http://www.w3.org/2001/sw/DataAccess/tests/test-manifest#")

PATTERN = regex(r'^s_(?P<bad>bad_)?(?P<name>.*)\.ldpatch$')

def main():
    "Generate manifest-syntax.ttl from s-*.ldpatch"
    logging.basicConfig(level=logging.INFO)

    g = Graph()
    g.add((MANIFEST_SYNTAX_IRI, RDF.type, MF.Manifest))
    g.add((MANIFEST_SYNTAX_IRI, RDFS.comment,
           Literal("Syntax tests for LD Patch")))

    entries = []

    for filename in listdir(TESTSUITE_PATH):
        match = PATTERN.match(filename)
        if not match:
            continue
        LOG.info("found %s", filename)

        bad, name = match.groups()
        entry = HASH[name]
        etype = NS.NegativeSyntaxTest if bad else NS.PositiveSyntaxTest
        comment = make_comment(filename, name)

        g.add((entry, RDF.type, etype))
        g.add((entry, MF.name, Literal(name)))
        g.add((entry, RDFS.comment, Literal(comment)))
        g.add((entry, MF.action, FILE[filename]))
        entries.append(entry)

    listname = BNode()
    Collection(g, listname, entries)
    g.add((MANIFEST_SYNTAX_IRI, MF.entries, listname))

    g.namespace_manager.bind("mf", MF)
    g.namespace_manager.bind("", NS)
    outttl = g.serialize(format="turtle")
    outttl = (outttl.decode("utf-8") # relativize all IRIS that need to
              .replace("<" + MANIFEST_SYNTAX_IRI, "<")
              .replace("<file://" + TESTSUITE_PATH + "/", "<")
             ).encode("utf-8")
    with open(MANIFEST_SYNTAX_PATH, "w") as fout:
        fout.write(outttl)

def make_comment(filename, name, path=TESTSUITE_PATH):
    "Build the comment for a given test file"
    comment = name.replace("_", " ")
    with open(join(path, filename)) as f:
        firstline = f.readline()
    if firstline[:1] == "#":
        comment += " ({})".format(firstline[:0].strip())
    return comment

if __name__ == "__main__":
    main()
