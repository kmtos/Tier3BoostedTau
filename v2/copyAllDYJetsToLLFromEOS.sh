#!/bin/bash

eval `scramv1 runtime -sh`
for sample in "10To50" "50"
  do
  for MTBin in high low
    do
    cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadAnalysis_${MTBin}MT_DYJetsToLL_M-${sample}_v2.root /mnt/hadoop/store/user/kmtos/data1/kmtos/DYJetsToLL/analysis/MT_DYJetsToLL_M-${sample}_v2.root /data1/kmtos/DYJetsToLL/analysis/
    rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadAnalysis_${MTBin}MT_DYJetsToLL_M-${sample}_v2.root
done
done

exit 0
