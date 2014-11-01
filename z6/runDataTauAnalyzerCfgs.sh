#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

for file in `ls -alh *SingleMu*.py | grep -v nonIsoW | awk '{ print $9 }'`
  do
  outFile=`echo $file | sed -e "s%\.py%.txt%"`
  isIso=`echo $file | sed -e "s%.*\(iso\).*%\1%"`
#  if [ "$isIso" != "iso" ] #BLINDED!!!
#      then
      cmsRun $file > $outFile
#  else
#      echo "Not running script $file due to blinding requirement"
#  fi
done

exit 0
