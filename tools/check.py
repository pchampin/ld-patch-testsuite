#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Transform the original manifest.ttl of the Turtle test-suite
into a manifest-ldpatch.ttl adapted to LD Patch.
"""

# pylint: disable=C0103
import logging
from os import listdir
from os.path import abspath, dirname, exists, join
from re import compile as regex
from urllib import pathname2url

from rdflib import Graph, Namespace, RDF, URIRef

LOG = logging.getLogger("gen-syntax-manifest")

MF = Namespace("http://www.w3.org/2001/sw/DataAccess/tests/test-manifest#")

TESTSUITE_PATH = dirname(dirname(abspath(__file__)))
TURTLE_PATH = join(TESTSUITE_PATH, "turtle")
MANIFEST_PATH = join(TESTSUITE_PATH, "manifest.ttl")
MANIFEST_SYNTAX_PATH = join(TESTSUITE_PATH, "manifest-syntax.ttl")
MANIFEST_TURTLE_PATH = join(TURTLE_PATH, "manifest.ttl")
MANIFEST_TURTLE_LDPATCH_PATH = join(TURTLE_PATH, "manifest-ldpatch.ttl")

def p2i(path):
    "Convert path to IRI"
    return URIRef("file://{}".format(pathname2url(path)))

def main():
    "Detect all orphan files and entries"
    g = Graph()
    for manifest in [MANIFEST_PATH, MANIFEST_SYNTAX_PATH,
                     MANIFEST_TURTLE_LDPATCH_PATH,]:
        g.load(manifest, format="turtle")
        LOG.debug("loaded %s", manifest)
    for manifest in [MANIFEST_TURTLE_PATH,]:
        if exists(manifest):
            g.load(manifest, format="turtle")
            LOG.debug("loaded %s", manifest)

    # looking for entries that are not part of an mf:entry list
    for subj, _, _ in g.triples((None, MF.action, None)):
        if not list(g.triples((None, RDF.first, subj))):
            print subj

    # looking for files that are not referenced
    FILTER = regex(r'.*\.(ttl|nt|ldpatch)$')
    for foldername in (TESTSUITE_PATH, TURTLE_PATH):
        for filename in listdir(foldername):
            if not FILTER.match(filename):
                continue
            if filename.startswith("manifest"):
                continue
            iri = p2i(join(foldername, filename))
            if not list(g.triples((None, None, iri))):
                print iri

    # checking that all entries have the correct name
    for subj, _, obj in g.triples((None, MF.name, None)):
        if subj.rsplit("#",1)[1] != unicode(obj):
            print "WRONG NAME for ", subj



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    main()
