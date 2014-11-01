#!/bin/bash

eval `scramv1 runtime -sh`
for sample in "10To50" "50"
  do
  for MTBin in high low
    do
    cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/z6/muHadAnalysis_${MTBin}MT_DYJetsToLL_M-${sample}_z6.root /mnt/hadoop/store/user/kmtos/data1/kmtos/DYJetsToLL/analysis/MT_DYJetsToLL_M-${sample}_z6.root /data1/kmtos/DYJetsToLL/analysis/
    rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/z6/muHadAnalysis_${MTBin}MT_DYJetsToLL_M-${sample}_z6.root
done
done

exit 0
