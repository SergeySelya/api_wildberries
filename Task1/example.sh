#!/bin/bash
file1=$1
file2=$2
if cmp -s "$file1" "$file2"; then
    echo "Files are identical."
else
    echo "Files are different."
fi