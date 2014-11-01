#!/bin/bash

if [ $# -gt 3 ]
    then
    echo "Usage: ./generateZZTauAnalyzerCfgs.sh <version> <template cfg> [reweightOnly]"
    exit 0
fi

####STUFF TO CONFIGURE####

#version
version=$1
templateCfg=$2
infoTag=""
reweightOnly=0
if [ "$3" == "reweightOnly" ]
    then
    reweightOnly=1
fi
dir=$version

#number of samples
nSamples=1
iBeg=0
iEnd=`expr $nSamples - 1`

#input file prefix
inputFilePrefix="file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/ZZ_TuneZ2star_8TeV_pythia6_tauola-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_"

#CleanJets output file prefix
#cleanJetsOutputFilePrefix="`pwd`/${dir}/"
cleanJetsOutputFilePrefix="file:/`pwd`/${dir}/"

#TauAnalyzer output file prefix
#tauAnalyzerOutputFilePrefix="/data1/yohay/ZZ/analysis/"
tauAnalyzerOutputFilePrefix="file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/${version}/"

#EDM output file prefix
EDMOutputFilePrefix="file:/mnt/hadoop/store/user/kmtos/data1/kmtos/ZZ/EDM_files/"

####VECTORS OF QUANTITIES FOR EACH SAMPLE####

#vector of input file blocks for each sample
inputFileBlocks=( "readFiles.extend([\n    '${inputFilePrefix}100_1_pC0.root',\n    '${inputFilePrefix}101_1_rgy.root',\n    '${inputFilePrefix}102_1_lTn.root',\n    '${inputFilePrefix}103_1_ERR.root',\n    '${inputFilePrefix}104_1_vwQ.root',\n    '${inputFilePrefix}105_1_vTd.root',\n    '${inputFilePrefix}106_1_HC5.root',\n    '${inputFilePrefix}107_1_Em2.root',\n    '${inputFilePrefix}108_2_r0O.root',\n    '${inputFilePrefix}109_1_f9v.root',\n    '${inputFilePrefix}10_1_pa3.root',\n    '${inputFilePrefix}110_1_rFH.root',\n    '${inputFilePrefix}111_2_amQ.root',\n    '${inputFilePrefix}112_1_vSY.root',\n    '${inputFilePrefix}113_1_SOG.root',\n    '${inputFilePrefix}114_1_HZt.root',\n    '${inputFilePrefix}115_1_72c.root',\n    '${inputFilePrefix}116_1_ubH.root',\n    '${inputFilePrefix}117_1_amq.root',\n    '${inputFilePrefix}118_1_FG4.root',\n    '${inputFilePrefix}119_1_WwR.root',\n    '${inputFilePrefix}11_1_Azo.root',\n    '${inputFilePrefix}120_1_LNh.root',\n    '${inputFilePrefix}121_1_sqk.root',\n    '${inputFilePrefix}122_1_lKK.root',\n    '${inputFilePrefix}123_1_JNF.root',\n    '${inputFilePrefix}124_1_EbS.root',\n    '${inputFilePrefix}125_1_h1g.root',\n    '${inputFilePrefix}126_1_7wf.root',\n    '${inputFilePrefix}127_1_gYd.root',\n    '${inputFilePrefix}128_1_N1k.root',\n    '${inputFilePrefix}129_1_fxP.root',\n    '${inputFilePrefix}12_1_P9X.root',\n    '${inputFilePrefix}130_1_4jd.root',\n    '${inputFilePrefix}131_1_pvq.root',\n    '${inputFilePrefix}132_1_S1h.root',\n    '${inputFilePrefix}133_1_hWz.root',\n    '${inputFilePrefix}134_1_jpl.root',\n    '${inputFilePrefix}135_1_9CJ.root',\n    '${inputFilePrefix}136_1_0B3.root',\n    '${inputFilePrefix}137_1_C9c.root',\n    '${inputFilePrefix}138_1_GFH.root',\n    '${inputFilePrefix}139_1_S0D.root',\n    '${inputFilePrefix}13_1_eA3.root',\n    '${inputFilePrefix}140_2_xUM.root',\n    '${inputFilePrefix}141_1_YlX.root',\n    '${inputFilePrefix}142_1_Ucn.root',\n    '${inputFilePrefix}143_1_VgE.root',\n    '${inputFilePrefix}144_1_wJo.root',\n    '${inputFilePrefix}145_1_bfA.root',\n    '${inputFilePrefix}146_1_jNk.root',\n    '${inputFilePrefix}147_1_j1C.root',\n    '${inputFilePrefix}148_1_0P8.root',\n    '${inputFilePrefix}149_1_X0Q.root',\n    '${inputFilePrefix}14_1_qOJ.root',\n    '${inputFilePrefix}150_1_9gf.root',\n    '${inputFilePrefix}151_1_ZKr.root',\n    '${inputFilePrefix}152_1_rQX.root',\n    '${inputFilePrefix}153_1_zmD.root',\n    '${inputFilePrefix}154_1_VH5.root',\n    '${inputFilePrefix}155_1_vl2.root',\n    '${inputFilePrefix}156_1_CgT.root',\n    '${inputFilePrefix}157_1_ba6.root',\n    '${inputFilePrefix}158_2_LAK.root',\n    '${inputFilePrefix}159_1_vg5.root',\n    '${inputFilePrefix}15_1_Pqi.root',\n    '${inputFilePrefix}160_1_7It.root',\n    '${inputFilePrefix}161_1_vJ7.root',\n    '${inputFilePrefix}162_1_LZU.root',\n    '${inputFilePrefix}163_1_qzj.root',\n    '${inputFilePrefix}164_1_CTS.root',\n    '${inputFilePrefix}165_1_3ma.root',\n    '${inputFilePrefix}166_1_vaN.root',\n    '${inputFilePrefix}167_1_rWg.root',\n    '${inputFilePrefix}168_1_uMK.root',\n    '${inputFilePrefix}169_1_7Kd.root',\n    '${inputFilePrefix}16_1_jA7.root',\n    '${inputFilePrefix}170_1_Ouj.root',\n    '${inputFilePrefix}171_1_wrq.root',\n    '${inputFilePrefix}172_1_SL8.root',\n    '${inputFilePrefix}173_1_CWU.root',\n    '${inputFilePrefix}174_1_sQL.root',\n    '${inputFilePrefix}175_1_sIF.root',\n    '${inputFilePrefix}176_1_F57.root',\n    '${inputFilePrefix}177_1_oIK.root',\n    '${inputFilePrefix}178_1_473.root',\n    '${inputFilePrefix}179_1_9a2.root',\n    '${inputFilePrefix}17_1_L1m.root',\n    '${inputFilePrefix}180_2_Kdx.root',\n    '${inputFilePrefix}181_1_nMw.root',\n    '${inputFilePrefix}182_2_RNN.root',\n    '${inputFilePrefix}183_1_cOK.root',\n    '${inputFilePrefix}184_2_gka.root',\n    '${inputFilePrefix}185_2_Vpz.root',\n    '${inputFilePrefix}186_2_NkF.root',\n    '${inputFilePrefix}187_2_tg9.root',\n    '${inputFilePrefix}188_2_GMp.root',\n    '${inputFilePrefix}189_2_uqr.root',\n    '${inputFilePrefix}18_1_r5e.root',\n    '${inputFilePrefix}190_1_Wgf.root',\n    '${inputFilePrefix}191_1_JIZ.root',\n    '${inputFilePrefix}192_1_epo.root',\n    '${inputFilePrefix}193_1_HXq.root',\n    '${inputFilePrefix}194_2_BQT.root',\n    '${inputFilePrefix}195_2_SRl.root',\n    '${inputFilePrefix}196_1_qfd.root',\n    '${inputFilePrefix}197_1_ZdP.root',\n    '${inputFilePrefix}198_2_4Q0.root',\n    '${inputFilePrefix}199_1_MFY.root',\n    '${inputFilePrefix}19_1_JvA.root',\n    '${inputFilePrefix}1_1_pHq.root',\n    '${inputFilePrefix}200_1_e8c.root',\n    '${inputFilePrefix}201_2_vxY.root',\n    '${inputFilePrefix}202_1_Mp7.root',\n    '${inputFilePrefix}20_1_R9A.root',\n    '${inputFilePrefix}21_1_ffu.root',\n    '${inputFilePrefix}22_1_sJx.root',\n    '${inputFilePrefix}23_1_TBu.root',\n    '${inputFilePrefix}24_1_LJx.root',\n    '${inputFilePrefix}25_1_ImJ.root',\n    '${inputFilePrefix}26_1_0LW.root',\n    '${inputFilePrefix}27_1_tTM.root',\n    '${inputFilePrefix}28_1_EXG.root',\n    '${inputFilePrefix}29_1_H1R.root',\n    '${inputFilePrefix}2_1_5R2.root',\n    '${inputFilePrefix}30_1_m6t.root',\n    '${inputFilePrefix}31_1_Tj4.root',\n    '${inputFilePrefix}32_1_fMQ.root',\n    '${inputFilePrefix}33_1_vOG.root',\n    '${inputFilePrefix}34_1_gq6.root',\n    '${inputFilePrefix}35_1_ErW.root',\n    '${inputFilePrefix}36_1_U9j.root',\n    '${inputFilePrefix}37_1_lLG.root',\n    '${inputFilePrefix}38_1_LgE.root',\n    '${inputFilePrefix}39_1_tUb.root',\n    '${inputFilePrefix}3_1_FOk.root',\n    '${inputFilePrefix}40_1_i9P.root',\n    '${inputFilePrefix}41_1_NN7.root',\n    '${inputFilePrefix}42_1_wWn.root',\n    '${inputFilePrefix}43_1_Btx.root',\n    '${inputFilePrefix}44_1_Hl4.root',\n    '${inputFilePrefix}45_1_Ux2.root',\n    '${inputFilePrefix}46_1_PrZ.root',\n    '${inputFilePrefix}47_1_IG0.root',\n    '${inputFilePrefix}48_1_i15.root',\n    '${inputFilePrefix}49_1_Wkr.root',\n    '${inputFilePrefix}4_1_2PS.root',\n    '${inputFilePrefix}50_1_R35.root',\n    '${inputFilePrefix}51_1_bv2.root',\n    '${inputFilePrefix}52_1_KoP.root',\n    '${inputFilePrefix}53_1_RJn.root',\n    '${inputFilePrefix}54_1_zuP.root',\n    '${inputFilePrefix}55_1_azp.root',\n    '${inputFilePrefix}56_1_VNI.root',\n    '${inputFilePrefix}57_1_p4U.root',\n    '${inputFilePrefix}58_1_4cs.root',\n    '${inputFilePrefix}59_1_1g6.root',\n    '${inputFilePrefix}5_1_X5W.root',\n    '${inputFilePrefix}60_1_y4V.root',\n    '${inputFilePrefix}61_1_QhA.root',\n    '${inputFilePrefix}62_1_iVT.root',\n    '${inputFilePrefix}63_1_Rtu.root',\n    '${inputFilePrefix}64_1_jMv.root',\n    '${inputFilePrefix}65_1_UFX.root',\n    '${inputFilePrefix}66_1_tfP.root',\n    '${inputFilePrefix}67_1_gNl.root',\n    '${inputFilePrefix}68_1_2U7.root',\n    '${inputFilePrefix}69_1_s0x.root',\n    '${inputFilePrefix}6_1_lj6.root',\n    '${inputFilePrefix}70_1_2lm.root',\n    '${inputFilePrefix}71_1_Hpa.root',\n    '${inputFilePrefix}72_1_5cu.root',\n    '${inputFilePrefix}73_2_oXb.root',\n    '${inputFilePrefix}74_1_r2r.root',\n    '${inputFilePrefix}75_1_fwt.root',\n    '${inputFilePrefix}76_1_saZ.root',\n    '${inputFilePrefix}77_1_4VR.root',\n    '${inputFilePrefix}78_1_fZQ.root',\n    '${inputFilePrefix}79_1_MSb.root',\n    '${inputFilePrefix}7_1_lPY.root',\n    '${inputFilePrefix}80_1_i3m.root',\n    '${inputFilePrefix}81_1_AtC.root',\n    '${inputFilePrefix}82_1_Lqj.root',\n    '${inputFilePrefix}83_1_7V0.root',\n    '${inputFilePrefix}84_1_Ahe.root',\n    '${inputFilePrefix}85_1_C1F.root',\n    '${inputFilePrefix}86_1_iGe.root',\n    '${inputFilePrefix}87_1_XMm.root',\n    '${inputFilePrefix}88_1_fBA.root',\n    '${inputFilePrefix}89_1_Eby.root',\n    '${inputFilePrefix}8_1_Tj3.root',\n    '${inputFilePrefix}90_1_Kfz.root',\n    '${inputFilePrefix}91_1_FPf.root',\n    '${inputFilePrefix}92_1_FFZ.root',\n    '${inputFilePrefix}93_1_Yiv.root',\n    '${inputFilePrefix}94_1_vNs.root',\n    '${inputFilePrefix}95_1_Wwu.root',\n    '${inputFilePrefix}96_1_kZu.root',\n    '${inputFilePrefix}97_1_kZv.root',\n    '${inputFilePrefix}98_1_lGG.root',\n    '${inputFilePrefix}99_1_ETN.root',\n    '${inputFilePrefix}9_1_0EE.root'\n    ])" )

#CleanJets output file
cleanJetsOutFiles=( "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_ZZ.root" )

#TauAnalyzer output files
highMTIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_highMT_ZZ_${version}.root" )
lowMTIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_lowMT_ZZ_${version}.root" )
highMTNonIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_highMT_ZZ_${version}.root" )
lowMTNonIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_lowMT_ZZ_${version}.root" )
nonIsoReweightTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_ZZ_${version}.root" )
highMTAllTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadAnalysis_highMT_ZZ_${version}.root" )
lowMTAllTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadAnalysis_lowMT_ZZ_${version}.root" )

#EDM output files
EDMOutputFiles=( "${EDMOutputFilePrefix}ZZ${infoTag}_${version}.root" )

#samples
samples=( "ZZ" )

####GENERATION LOOP####

#change to working directory
mkdir -p $dir
cd $dir

#loop over number of samples
for i in `seq $iBeg $iEnd`
  do


  #generate cfg file for the isolated sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%HIGHMTNONISOTAUANALYZEROUTFILE%${highMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTALLTAUANALYZEROUTFILE%${highMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTISOTAUANALYZEROUTFILE%${highMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTNONISOTAUANALYZEROUTFILE%${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTALLTAUANALYZEROUTFILE%${lowMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTISOTAUANALYZEROUTFILE%${lowMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%HIGHMTSEQUENCE%process.highMTIsoTauAnalysisSequence%" -e "s%LOWMTSEQUENCE%process.lowMTIsoTauAnalysisSequence%"	-e "s%PUSCENARIO%S10%" -e "s%SAMPLE%%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_iso_cfg.py

  #generate cfg file for the non-isolated sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%HIGHMTNONISOTAUANALYZEROUTFILE%${highMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTALLTAUANALYZEROUTFILE%${highMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTISOTAUANALYZEROUTFILE%${highMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTNONISOTAUANALYZEROUTFILE%${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTALLTAUANALYZEROUTFILE%${lowMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTISOTAUANALYZEROUTFILE%${lowMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%HIGHMTSEQUENCE%process.highMTNonIsoTauAnalysisSequence%" -e "s%LOWMTSEQUENCE%process.lowMTNonIsoTauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%SAMPLE%%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_nonIso_cfg.py

  #generate cfg file for the non-isolated, reweighted sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%HIGHMTNONISOTAUANALYZEROUTFILE%${nonIsoReweightTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTALLTAUANALYZEROUTFILE%${highMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTISOTAUANALYZEROUTFILE%${highMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTNONISOTAUANALYZEROUTFILE%${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTALLTAUANALYZEROUTFILE%${lowMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTISOTAUANALYZEROUTFILE%${lowMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%HIGHMTSEQUENCE%process.highMTNonIsoTauAnalysisSequence%" -e "s%LOWMTSEQUENCE%process.lowMTNonIsoTauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%SAMPLE%%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_nonIsoReweight_cfg.py

  #generate cfg file for the sample with no isolation cut
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%HIGHMTNONISOTAUANALYZEROUTFILE%${highMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTALLTAUANALYZEROUTFILE%${highMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTISOTAUANALYZEROUTFILE%${highMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTNONISOTAUANALYZEROUTFILE%${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTALLTAUANALYZEROUTFILE%${lowMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTISOTAUANALYZEROUTFILE%${lowMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%HIGHMTSEQUENCE%process.highMTTauAnalysisSequence%" -e  "s%LOWMTSEQUENCE%process.lowMTTauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%SAMPLE%%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_all_cfg.py

  #generate iso+nonIso+reweight job submission script for LSF
  cat <<EOF > tauanalyzer_${samples[${i}]}_cfg.sh
#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

echo "Running tauanalyzer_${samples[${i}]}_cfg.sh"
jobDir="`pwd`"
fileNamePrefix="tauanalyzer_${samples[${i}]}"

eval \`scramv1 runtime -sh\`
cmsRun \${fileNamePrefix}_iso_cfg.py
echo "cmsRun \${fileNamePrefix}_iso_cfg.py DONE"
if [ $reweightOnly -eq 0 ]
    then
    echo "Just inside first if loop"
    cmsRun \${fileNamePrefix}_nonIso_cfg.py
    echo "cmsRun \${fileNamePrefix}_nonIso_cfg.py DONE"
fi
#cmsRun \${fileNamePrefix}_nonIsoReweight_cfg.py
#echo "cmsRun \${fileNamePrefix}_nonIsoReweight_cfg.py DONE"
exit 0
EOF
  chmod a+x tauanalyzer_${samples[${i}]}_cfg.sh

  #generate noIsoCut job submission script for LSF
  cat <<EOF > tauanalyzer_${samples[${i}]}_all_cfg.sh
#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

echo "Running tauanalyzer_${samples[${i}]}_all_cfg.sh"
jobDir="`pwd`"
fileNamePrefix="tauanalyzer_${samples[${i}]}"

eval \`scramv1 runtime -sh\`
cmsRun \${fileNamePrefix}_all_cfg.py 
echo "cmsRun \${fileNamePrefix}_all_cfg.py DONE"

exit 0
EOF
  chmod a+x tauanalyzer_${samples[${i}]}_all_cfg.sh
done

#generate run cfg that runs all files in the directory
cat <<EOF > runZZTauAnalyzerCfgs.sh
#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

for file in \`ls -alh *ZZ*.py | awk '{ print \$9 }'\`
  do
  outFile=\`echo \$file | sed -e "s%\.py%.txt%"\`

done

exit 0
EOF
chmod a+x runZZTauAnalyzerCfgs.sh

#generate script that submits all iso+nonIso+reweight jobs to LSF
cat <<EOF > submitZZTauAnalyzerJobs.sh
#!/bin/bash

for file in \`ls -alh tauanalyzer*ZZ*.sh | grep -v all | awk '{ print \$9 }'\`
  do
  jobName=\`echo \$file | sed -e "s%\(.*\)\.sh%\1%"\`
  echo "\$file"

  cat>Csubmit_\$jobName<<EOF
Universe   = vanilla
Executable = \$file
Log        = Csubmit_\$jobName.log
Output     = Csubmit_\$jobName.out
Error      = Csubmit_\$jobName.error
Queue
EOF

echo "EOF

echo \"generateZZTauAnalyzerCfgs.sh\"
condor_submit  Csubmit_\$jobName
done
exit 0" >> submitZZTauAnalyzerJobs.sh
chmod a+x submitZZTauAnalyzerJobs.sh

#generate script that submits all noIsoCut jobs to LSF
cat <<EOF > submitZZAllTauAnalyzerJobs.sh
#!/bin/bash

for file in \`ls -alh tauanalyzer*ZZ*all*.sh | awk '{ print \$9 }'\`
  do
  jobName=\`echo \$file | sed -e "s%\(.*\)\.sh%\1%"\`
  echo "\$file"

  cat>Csubmit_\$jobName<<EOF
Universe   = vanilla
Executable = \$file
Log        = Csubmit_\$jobName.log
Output     = Csubmit_\$jobName.out
Error      = Csubmit_\$jobName.error
Queue
EOF

echo "EOF

echo \"generateZZTauAnalyzerCfgs.sh\"
condor_submit  Csubmit_\$jobName
done
exit 0" >> submitZZAllTauAnalyzerJobs.sh
chmod a+x submitZZAllTauAnalyzerJobs.sh

#generate script that copies all iso+nonIso+reweight files locally from EOS
cat <<EOF > copyZZFromEOS.sh
#!/bin/bash

eval \`scramv1 runtime -sh\`
for sample in \`seq `expr $iBeg + 1` `expr $iEnd + 1`\`
  do
  #for cut in Iso NonIso NonIsoReweight
  for cut in Iso NonIso
    do
    for MTBin in high low
      do
      if [ "\$cut" != "NonIso" ] || [ $reweightOnly -eq 0 ]
          then
          cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/${version}/muHad\${cut}Analysis_\${MTBin}MT_ZZ_${version}.root /mnt/hadoop/store/user/kmtos/data1/`whoami`/ZZ/analysis/
          rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/${version}/muHad\${cut}Analysis_\${MTBin}MT_ZZ_${version}.root
      fi
    done
  done
done

exit 0
EOF
chmod a+x copyZZFromEOS.sh

#generate script that copies all noIsoCut files locally from EOS
cat <<EOF > copyAllZZFromEOS.sh
#!/bin/bash

eval \`scramv1 runtime -sh\`
for sample in \`seq `expr $iBeg + 1` `expr $iEnd + 1`\`
  do
  for MTBin in high low
    do
    cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/${version}/muHadAnalysis_\${MTBin}MT_ZZ_${version}.root /mnt/hadoop/store/user/kmtos/data1/`whoami`/ZZ/analysis/
    rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/${version}/muHadAnalysis_\${MTBin}MT_ZZ_${version}.root
  done
done

exit 0
EOF
chmod a+x copyAllZZFromEOS.sh

exit 0
