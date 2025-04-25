#!/bin/bash
files=$(find . -name "*.out")
for file in $files; do
echo $* >> ${file}
done