#!/bin/bash

eval `scramv1 runtime -sh`
for sample in "A" "B" "C" "D"
  do
  for MTBin in high low
    do
    cp -f  /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v1/nonIsoW_muHadAnalysis_${MTBin}MT_SingleMu_Run2012${sample}_v1.root /mnt/hadoop/store/user/kmtos/data1/kmtos/nonIsoWData/analysis/
    rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v1/nonIsoW_muHadAnalysis_${MTBin}MT_SingleMu_Run2012${sample}_v1.root
  done
done

exit 0
