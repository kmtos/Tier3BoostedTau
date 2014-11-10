#!/bin/bash

for file in `ls -alh *Wh1_a*_iso*.py | grep -v MET | awk '{ print $9 }'`
  do
  outFile=`echo $file | sed -e "s%\.py%.txt%"`
  echo "file=  $file"
  echo "Output file= $outFile"
  cmsRun $file >& $outFile &
done

exit 0
