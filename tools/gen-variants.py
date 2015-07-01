#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Transform the original manifest.ttl of the Turtle test-suite
into a manifest-ldpatch.ttl adapted to LD Patch.
"""

# pylint: disable=C0103
import logging
from os import listdir
from os.path import abspath, dirname, exists, getmtime, join
from re import compile as regex

LOG = logging.getLogger("gen-variants")

TESTSUITE_PATH = dirname(dirname(abspath(__file__)))

PATTERN = regex(r'^s_(bad_)?(?P<operation>[^_]*)_.*\.ldpatch$')

def main():
    "Generate variants for syntax tests"
    logging.basicConfig(level=logging.INFO)

    for filename in listdir(TESTSUITE_PATH):
        if filename.endswith(".v.ldpatch"):
            continue # this is a generated file
        match = PATTERN.match(filename)
        if not match:
            continue
        LOG.debug("Found %s", filename)

        _, operation = match.groups()
        if operation == "add":
            gen_variant(filename, "Add", "A")
            gen_variant(filename, "Add", "AddNew")
            gen_variant(filename, "Add", "AN")
            gen_variant(filename, "Add", "Delete")
            gen_variant(filename, "Add", "D")
            gen_variant(filename, "Add", "DeleteExisting")
            gen_variant(filename, "Add", "DE")
        elif operation == "cut":
            gen_variant(filename, "Cut", "C")
        elif operation == "updatelist":
            gen_variant(filename, "UpdateList", "UL")
        else:
            pass

def gen_variant(src_filename, src_op, dst_op):
    "Generate the variant file for src_filename, replacing src_op by dst_op"
    dst_filename = src_filename \
        .replace("_{}_".format(src_op).lower(),
                 "_{}_".format(dst_op).lower(),
                 1) \
        .replace(".ldpatch", ".v.ldpatch")
    src_fullpath = join(TESTSUITE_PATH, src_filename)
    dst_fullpath = join(TESTSUITE_PATH, dst_filename)
    if exists(dst_fullpath) \
       and getmtime(src_fullpath) < getmtime(dst_fullpath):
        return

    with open(dst_fullpath, "w") as dstf:
        #dstf.write("#GENERATED from {} - DO NOT CHANGE\n"
        #           .format(src_filename))
        dstf.write("@prefix THIS_FILE_WAS_GENERATED__DO_NOT_CHANGE_IT: <>.\n")
        with open(src_fullpath) as srcf:
            for line in srcf:
                if line.startswith(src_op):
                    line = line.replace(src_op, dst_op, 1)
                dstf.write(line)

    LOG.info("Generated %s", dst_filename)
    return dst_filename


if __name__ == "__main__":
    main()
