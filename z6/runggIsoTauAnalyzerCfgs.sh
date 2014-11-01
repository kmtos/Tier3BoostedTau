#!/bin/bash

for file in `ls -alh *gg_a*_iso*.py | grep -v MET | awk '{ print $9 }'`
  do
  outFile=`echo $file | sed -e "s%\.py%.txt%"`
  echo "File running= $file"
  echo "Output file $outFile"
  cmsRun $file >& $outFile &
done

exit 0
