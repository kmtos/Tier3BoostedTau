#!/bin/bash

eval `scramv1 runtime -sh`
for sample in "A" "B" "C" "D"
  do
    #loop over number of subjobs
    for jInd in `seq 0 7`
      do
       #for cut in Iso NonIso NonIsoReweight #BLINDED!!!
      for cut in Iso NonIso
        do
        for MTBin in high low
          do
            if [ "$cut" != "NonIso" ] || [ 0 -eq 0 ]
            then
            cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/z6/muHad${cut}Analysis_${MTBin}MT_SingleMu_Run2012${sample}_${jInd}_z6.root /mnt/hadoop/store/user/kmtos/data1/kmtos/data/analysis/
            rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/z6/muHad${cut}Analysis_${MTBin}MT_SingleMu_Run2012${sample}_${jInd}_z6.root
            fi
        done
      done
   done
done

exit 0
