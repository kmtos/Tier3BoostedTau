#!/bin/bash

version=$1

cd $version
rm ${version}_TOTAL_ERROR_OUTPUT.out
files="$(ls -1 *.error)"
for file in $files; do
  ls $file
  cat $file >> ${version}_TOTAL_ERROR_OUTPUT.out
done


