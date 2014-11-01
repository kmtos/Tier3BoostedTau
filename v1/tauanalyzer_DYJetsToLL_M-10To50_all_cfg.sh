#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

echo "Running tauanalyzer_DYJetsToLL_M-10To50_all_cfg.sh"
jobDir="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v1"
fileNamePrefix="tauanalyzer_DYJetsToLL_M-10To50"

eval `scramv1 runtime -sh`
cmsRun ${fileNamePrefix}_all_cfg.py
echo "cmsRun ${fileNamePrefix}_all_cfg.py DONE"

exit 0
