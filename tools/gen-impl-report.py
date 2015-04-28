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

from rdflib import Graph, Namespace, RDFS
from rdflib.collection import Collection
from rdflib.namespace import DC

LOG = logging.getLogger("gen-syntax-manifest")

MF = Namespace("http://www.w3.org/2001/sw/DataAccess/tests/test-manifest#")

TESTSUITE_PATH = dirname(dirname(abspath(__file__)))
TURTLE_PATH = join(TESTSUITE_PATH, "turtle")
TESTSUITE_NS = Namespace("https://raw.githubusercontent.com/pchampin/ld-patch-testsuite/master/")

MANIFEST_PATH_BASE = (join(TESTSUITE_PATH, "manifest.ttl"),
                      TESTSUITE_NS["manifest.ttl"])
MANIFEST_SYNTAX_PATH_BASE = (join(TESTSUITE_PATH, "manifest-syntax.ttl"),
                             TESTSUITE_NS["manifest-syntax.ttl"])
MANIFEST_TURTLE_LDPATCH_PATH_BASE = (join(TURTLE_PATH, "manifest-ldpatch.ttl"),
                                     TESTSUITE_NS["turtle/manifest-ldpatch.ttl"])
ALL_MANIFESTS_PATH_BASE = [
    MANIFEST_PATH_BASE,
    MANIFEST_SYNTAX_PATH_BASE,
    MANIFEST_TURTLE_LDPATCH_PATH_BASE,
]

REPORTS_PATH = join(TESTSUITE_PATH, "reports")

EARL = Namespace("http://www.w3.org/ns/earl#")

def main():
    "Generate README.rst for all implementation reports"

    g = load_graph()
    softwares, tests, report = prepare_data(g)
    generate_html(g, softwares, tests, report)


def load_graph():
    """Load manifests and reports into a single graph, and return it"""

    g = Graph()
    g.bind("earl", EARL[""])
    g.bind("dc", DC[""])
    g.bind("mf", MF[""])
    g.bind("doap", "http://usefulinc.com/ns/doap#")
    g.bind("foaf", "http://xmlns.com/foaf/0.1/")

    for manifest_filename, manifest_iri in ALL_MANIFESTS_PATH_BASE:
        g.load(manifest_filename, format="turtle", publicID=manifest_iri)
        LOG.debug("loaded %s", manifest_filename)

    FILTER = regex(r'.*\.ttl$')
    for filename in listdir(REPORTS_PATH):
        if not FILTER.match(filename):
            continue
        report_path = join(REPORTS_PATH, filename)
        g.load(report_path, format="turtle",
               publicID=TESTSUITE_NS["reports/" + filename])
        LOG.debug("loaded %s", report_path)

    return g


def prepare_data(g):
    """Prepare and return

    - softwares: an ordered list of tuples describing the implementations
    - tests: an ordered list of test IRIs
    - report: a 2-level dict containing the outcomes of the tests,
      indexed as test-iri -> software-iri -> outcome
    """

    #### EXTRACTING DATA FROM GRAPH ####

    softwares = list(g.query("""SELECT ?software ?name ?homepage ?description ?passed
        {
            {
                SELECT ?software (COUNT(?assertion) as ?passed){
                    ?assertion
                      earl:subject ?software ;
                      earl:result [
                        earl:outcome earl:passed ] .
                } GROUP BY ?software
            }
            ?software
                doap:name ?name ;
                doap:homepage ?homepage ;
                doap:description ?description .
            [] foaf:primaryTopic ?software ; dc:issued ?issued .
        } ORDER BY ?issued
        """))

    tests = []
    for _, manifest in ALL_MANIFESTS_PATH_BASE:
        entrylist = g.value(manifest, MF.entries)
        tests.extend(Collection(g, entrylist))

    report = {}
    for test, subject, outcome in g.query("""SELECT ?test ?subject ?outcome
            {
                [
                    earl:test ?test ;
                    earl:subject ?subject ;
                    earl:result [ earl:outcome ?outcome ]
                ]
            } ORDER BY ?subject
            """):
        report_row = report[test] = report.get(test) or {}
        report_row[subject] = outcome

    return softwares, tests, report


def generate_html(g, softwares, tests, report):
    """Generate the ReST document of the report"""

    print """<!html>
    <html>
    <head>
      <meta charset="utf-8"/>
      <title>LD Patch Implementation Reports</title>
      <style type="text/css">
        th.test {
          text-align: right;
        }
        td.passed {
          text-align: center;
          background-color: darkGreen;
          color: white;
        }
        td.failed {
          text-align: center;
          background-color: red;
          color: black;
        }
        td.canttell {
          text-align: center;
          background-color: transparent;
          color: darkGrey;
        }
        table.box {
            width: 100%;
            border: 1px solid black;
            margin-bottom: 1ex;
        }
        table.box th {
            width: 10em;
        }

      </style>
    </head>
    <body>
      <h1>LD Patch Implementation Reports</h1>

      <p>This is the implementation report for
         the <a href="http://www.w3.org/TR/ldpatch">Linked Data Patch Format</a>.
         Instructions for submitting new implementations are
         <a href="https://github.com/pchampin/ld-patch-testsuite/blob/master/README.rst"
             >available here</a>.
         The raw data of the reports are
         <a href="https://github.com/pchampin/ld-patch-testsuite/tree/master/reports"
             >available here</a>.</p>"""

    print """
      <h2>Reports</h2>
      <table>
        <tr><th></th><th></th>"""

    for _, name, _, _, _ in softwares:
        print """<td><a href="#{name}">{name}</a></td>""".format(**locals())
    print """</tr>"""

    print """<tr><th></th><th>#passed</th>"""
    for _, _, _, _, passed in softwares:
        print """<th>{passed}</th>""".format(**locals())
    print """</tr>"""

    for test in tests:
        report_row = report.get(test, {})
        name = g.value(test, MF.name)
        passed = len([ val for val in report_row.values() if val == EARL.passed ])
        print """<tr><th class="test" id="{name}-reports">""" \
              """<a href="#{name}-desc">{name}</a></th>""" \
              """<th>{passed}</th>""".format(**locals()),

        for software, _, _, _, _ in softwares:
            outcome = report_row.get(software)
            if outcome == EARL.passed:
                cls = "passed"
                val = "✓"
            elif outcome == EARL.failed:
                cls = "failed"
                val = "✗"
            else:
                cls = "canttell"
                val = "?"
            print """<td class="{cls}">{val}</td>""".format(**locals())
        print """</tr>"""
    print """</table>"""

    print """<h2>Implementations</h2>"""

    total = len(tests)
    for software, name, homepage, description, passed in softwares:
        print """<table class="box" id="{name}">
                 <tr><th>Name</th><td><a href="#{name}">{name}</a></td></tr>
                 <tr><th>Description</th><td>{description}</td></tr>
                 <tr><th>Homepage</th>
                     <td><tt><a href="{homepage}">{homepage}</a></tt></td></tr>
                 <tr><th>Passed</th><td>{passed}/{total}</td></tr>
                 </table>""".format(**locals())

    print """<h2>Tests</h2>"""

    total = len(softwares)
    for test in tests:
        name = g.value(test, MF.name)
        description = g.value(test, RDFS.comment).encode("utf-8")
        passed = len([ val for val in report.get(test, {}).values() if val == EARL.passed ])
        print """<table class="box" id="{name}-desc">
                 <tr><th>Name</th><td><a href="#{name}-desc">{name}</a></td></tr>
                 <tr><th>Description</th><td>{description}</td></tr>
                 <tr><th>Passed</th>
                     <td><a href="#{name}-reports">{passed}/{total}</a></td></tr>
                 </table>""".format(**locals())



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    main()
