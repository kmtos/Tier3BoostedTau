#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

for file in `ls -alh *ZZ*.py | awk '{ print $9 }'`
  do
  outFile=`echo $file | sed -e "s%\.py%.txt%"`

done

exit 0
