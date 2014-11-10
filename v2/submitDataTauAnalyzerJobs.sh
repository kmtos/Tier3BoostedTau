#!/bin/bash

for file in `ls -alh tauanalyzer*SingleMu*.sh | grep -v all | grep -v nonIsoW | awk '{ print $9 }'`
  do
  jobName=`echo $file | sed -e "s%\(.*\)\.sh%\1%"`
  echo "$file"

  cat>Csubmit_$jobName<<EOF
Universe   = vanilla
Executable = $file
Log        = Csubmit_$jobName.log
Output     = Csubmit_$jobName.out
Error      = Csubmit_$jobName.error
Queue
EOF

echo "generateDataTauAnalyzerCfgs.sh"
condor_submit  Csubmit_$jobName
done
exit 0
