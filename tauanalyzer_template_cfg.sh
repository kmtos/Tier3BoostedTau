#!/bin/bash

jobDir="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/DIR"
fileNamePrefix="tauanalyzer_template_cfg_JOB"
outputFilePrefix="DIR_tau_analysis_JOB"
outputFile="${outputFilePrefix}.root"

cd $jobDir
eval `scramv1 runtime -sh`
cd -
cp $jobDir/$fileNamePrefix.py .
cmsRun $fileNamePrefix.py
cp -f $outputFile /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/
rm $outputFile $outputFilePrefix.txt

exit 0
