#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

echo "Running tauanalyzer_WW_all_cfg.sh"
jobDir="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2"
fileNamePrefix="tauanalyzer_WW"

eval `scramv1 runtime -sh`
cmsRun ${fileNamePrefix}_all_cfg.py 
echo "cmsRun ${fileNamePrefix}_nonIsoReweight_cfg.py DONE"
exit 0
