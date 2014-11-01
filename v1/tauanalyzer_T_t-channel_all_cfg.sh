#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

echo "Running tauanalyzer_T_t-channel_all_cfg.sh"
jobDir="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v1"
fileNamePrefix="tauanalyzer_T_t-channel"

eval `scramv1 runtime -sh`
cmsRun ${fileNamePrefix}_all_cfg.py 
echo "cmsRun ${fileNamePrefix}_all_cfg.py DONE"

exit 0