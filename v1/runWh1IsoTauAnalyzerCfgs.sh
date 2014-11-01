#!/bin/bash

for file in `ls -alh *Wh1_a*_iso*.py | grep -v MET | awk '{ print $9 }'`
  do
  outFile=`echo $file | sed -e "s%\.py%.txt%"`
  echo "file=  "
  echo "Output file= "
  cmsRun $file >& $outFile &
done

exit 0
