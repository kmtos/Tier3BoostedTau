#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

for file in `ls -alh *W[0-9]JetsToLNu*.py | awk '{ print $9 }'`
  do
  outFile=`echo $file | sed -e "s%\.py%.txt%"`
  cmsRun $file > $outFile
done

exit 0
