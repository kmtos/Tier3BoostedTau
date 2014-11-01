#!/bin/bash
echo "Running tauanalyzer_W2JetsToLNu_all_cfg.sh"
jobDir="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/z6"
fileNamePrefix="tauanalyzer_W2JetsToLNu"

eval `scramv1 runtime -sh`
cmsRun ${fileNamePrefix}_all_cfg.py
echo "cmsRun ${fileNamePrefix}_all_cfg.py DONE"
exit 0
