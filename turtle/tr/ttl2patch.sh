#!/bin/sh
#
# convert TTL on stdin into LD Patch on stdout
#
# used by convert-all.sh

# extract turtle-style prefix
cat "$1" | grep -a '^@prefix'
# extract and convert sparql-style prefix
cat "$1" | grep -ai '^PREFIX' | sed 's/......\(.*\)/@prefix\1 ./'
# embed add into graph statement
echo "Add {"
cat "$1" | grep -av '^@prefix' | grep -avi '^PREFIX' | sed 's/^@\?base/# &/i'
echo "} ."
 
