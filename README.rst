=====================
 LD Patch Test Suite
=====================

This is the test suite for the `Linked Data Patch Format`_.

.. contents::


General instructions for running the LD Patch Test Suite
========================================================

This test suite is described by a manifest file ``manifest.ttl``
expressed in `Turtle`_,
and using the same vocabularies as the `SPARQL1.1 Test Suite`_
(see also the `RDF Test Suite`_).

Namespaces
----------

The following namespaces are declared in the manifest file,
and are used along this documentation:

.. code::

  @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
  @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
  @prefix mf: <http://www.w3.org/2001/sw/DataAccess/tests/test-manifest#> .
  @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
  @prefix : <manifest.ttl#> .

Note that terms in the empty namespace (``:``)
are specific to this test suite and are defined locally in the manifest
(*i.e.* through a relative IRI).


Structure of the manifest
-------------------------

The manifest has a header (as below), and lists:

* a number of ancillary manifest files (``mf:include``)
  that contain additional tests to include in the test suite,
  and comply with the same syntax, and

* a number of entries describing individual tests.

.. code::

   <>  rdf:type mf:Manifest ;
       rdfs:comment "LD-Patch tests" ;
       mf:include (
           ....
       ) ;
       mf:entries
       (
           ....
       ).

File names
----------

Typically, in the test case suite,
we use the following suffixes to indicate different file types:

.. list-table::
  :widths: 1 7

  * - ``.ttl``
    - files describing RDF graphs in the `Turtle`_ syntax
  * - ``.nt``
    - files describing RDF graphs in the `N-Triples`_ syntax
  * - ``.ldpatch``
    - files describing a patch in the `LD Patch`_ syntax

Syntax tests
------------

Syntax tests all have the same structure, illustrated below:

.. code::

    <#a_var_as_subject.v> a :PositiveSyntaxTest ;
        mf:name "a_var_as_subject.v" ;
        rdfs:comment "a var as subject.v ()" ;
        mf:action <s_a_var_as_subject.v.ldpatch> ;
        .

Each test has a *name*, an optional *comment*,
and an *action* that is a file to be parsed according to the LD-Patch syntax.
For ``:PositiveSyntaxTest``, that file must be successfully parsed,
while for ``:NegativeSyntaxTest``, that file must be rejected by the parser
(or at least recognized as a non-compliant file).

Note that for LD Patch servers,
the status code for a negative syntax test must always be 400 (Bad Request).

Evaluation tests
----------------

Evaluation tests all have the same structure, illustrated below:

.. code::

    <#empty> rdf:type :PositiveEvaluationTest ;
       mf:name      "empty" ;
       rdfs:comment "Empty patch" ;
       mf:action [
         :data  <1triple.nt> ;
         :patch <s_empty_patch.ldpatch> 
       ];
       mf:result <1triple.nt>
       .

Each test has a *name*, an optional *comment*, and an *action*.
The action has two mandatory properties:
``:data`` points to a file describing the target RDF graph,
and ``:patch`` points to a file describing the patch to apply to that target graph.
The action may also have an additional ``:base`` property,
that must then be used as the base IRI to parse the two files above
(else, the original IRI of the target graph file must be used).

Evaluation tests with type ``:PositiveEvaluationTest`` also have a *result*.
It is a file describing the expected RDF graph after applying the patch to the target graph.

Evaluation tests with type ``:NegativeEvaluationTest`` have no result,
as they are supposed to fail, and the target graph must not be modified.
They have a ``:statusCode`` property,
indicating which HTTP status an LD Patch server must return.

Implementation reports
======================

Implementation reports will be available `there </pchampin/ld-patch-testsuite/tree/master/reports>`_ .

Instructions for submitting implementation reports
--------------------------------------------------

Reports should be submitted to public-ldp-comments@w3.org
as a `Turtle`_ file using the `EARL`_ vocabulary.
and include an ``earl:Assertion`` for each test,
referencing the test resource from the associated manifest and the test subject being reported upon.
Note that, in that file, the base IRI of the test suite
(and hence of every indivudual test) must be 
https://raw.githubusercontent.com/pchampin/ld-patch-testsuite/master/ .

.. warning::

   Should the test-suite be hosted somehere else?

An example test entry is be the following:

.. code::

  [ a earl:Assertion;
    earl:assertedBy <http://champin.net/#pa>;
    earl:subject <https://github.com/pchampin/ld-patch-py>;
    earl:test <https://raw.githubusercontent.com/pchampin/ld-patch-testsuite/master/manifest.ttl#empty>;
    earl:result [
      a earl:TestResult;
      earl:outcome earl:passed;
      dc:date "2015-04-27T11:28:00"^^xsd:dateTime];
    earl:mode earl:automatic ] .

The Test Subject should be defined as a `DOAP`_ project,
including the name, homepage and developer(s) of the software. Optionally, including the project description and programming language. An example test subject description is the following:

.. code::

  <> foaf:primaryTopic <https://github.com/pchampin/ld-patch-py> ;
    dc:issued "2015-04-27T11:28:00"^^xsd:dateTime ;
    foaf:maker <http://champin.net/#pa> .

  <https://github.com/pchampin/ld-patch-py> a doap:Project, earl:TestSubject, earl:Software ;
    doap:name          "ld-patch-py" ;
    doap:homepage      <https://github.com/pchampin/ld-patch-py> ;
    doap:license       <http://www.gnu.org/licenses/lgpl-3.0.html> ;
    doap:description   "ld-patch-py is a Python processor for LD Patch, based on RDFLib" ;
    doap:created       "2014-11-11"^^xsd:date ;
    doap:programming-language "Python" ;
    doap:implements    <http://www.w3.org/TR/ldpatch/> ;
    doap:category      <http://dbpedia.org/resource/Resource_Description_Framework>,
                       <http://dbpedia.org/resource/Python_(programming_language)> ;
    doap:developer     <http://champin.net/#pa> ;
    dc:title           "ld-patch-py" ;
    dc:description     "ld-patch-py is a Python processor for LD Patch, based on RDFLib" ;
    dc:date            "2014-11-11"^^xsd:date ;
    .

The software developer,
either an organization or one or more individuals should be referenced from ``doap:developer`` using `FOAF`_.
For example:

.. code::

  <http://champin.net#pa> a foaf:Person, earl:Assertor;
    foaf:name "Pierre-Antoine Champin";
    foaf:homepage <http://champin.net/> .


.. _Linked Data Patch Format: http://www.w3.org/TR/ldpatch/
.. _Turtle: http://www.w3.org/TR/turtle/
.. _SPARQL1.1 Test Suite: http://www.w3.org/2009/sparql/docs/tests/README.html
.. _RDF Test Suite: http://www.w3.org/TR/2014/NOTE-rdf11-testcases-20140225/
.. _N-Triples: http://www.w3.org/TR/n-triples/
.. _LD Patch: http://www.w3.org/TR/ldpatch/
.. _EARL: http://www.w3.org/TR/EARL10-Schema/
.. _DOAP: https://github.com/edumbill/doap/wiki
.. _FOAF: http://xmlns.com/foaf/spec/
