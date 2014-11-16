#!/bin/sh
#
# convert all .ttl on .ldpatch files (except for manifest*.ttl)
#

TRPATH="`dirname "$0"`"
for i in *.ttl; do
    PATCHFILENAME="`basename "$i" .ttl`.ldpatch"
    "$TRPATH/ttl2patch.sh" "$i" > "$PATCHFILENAME"
    echo "$PATCHFILENAME"
done
# rm spurious converted files
rm manifest*.ldpatch
 
