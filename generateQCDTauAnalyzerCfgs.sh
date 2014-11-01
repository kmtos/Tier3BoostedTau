#!/bin/bash

if [ $# -gt 3 ]
    then
    echo "Usage: ./generateQCDTauAnalyzerCfgs.sh <version> <template cfg> [reweightOnly]"
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
nSamples=11
iBeg=0
iEnd=`expr $nSamples - 1`

#input file prefix
inputFilePrefix="file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/NMSSM_files/"

#input file suffix
inputFileSuffix="_MuEnrichedPt5_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v1/"

#CleanJets output file prefix
#cleanJetsOutputFilePrefix="`pwd`/${dir}/"
cleanJetsOutputFilePrefix="file:/`pwd`/${dir}/"

#TauAnalyzer output file prefix
#tauAnalyzerOutputFilePrefix="/data1/yohay/QCD/analysis/"
tauAnalyzerOutputFilePrefix="file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/muHad_files/"

#EDM output file prefix
EDMOutputFilePrefix="file:/mnt/hadoop/store/user/kmtos/data1/`whoami`/QCD/EDM_files/"

####VECTORS OF QUANTITIES FOR EACH SAMPLE####

#vector of input file blocks for each sample
inputFileBlocks=( "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_10_1_jea.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_11_1_1uF.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_12_1_eQC.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_13_1_EF3.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_14_1_p2j.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_15_1_bFQ.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_16_1_sxT.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_17_1_KnV.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_18_1_9OD.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_19_1_ZhJ.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_1_1_3vl.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_20_1_1BJ.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_21_1_iuw.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_22_1_yLp.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_23_1_lgf.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_24_1_b1n.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_25_1_6T1.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_26_1_pUV.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_27_1_6Q5.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_28_1_tli.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_29_1_HAz.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_2_1_NPX.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_30_2_Rwx.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_31_2_oH5.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_32_2_YpC.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_33_1_020.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_34_1_kHZ.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_35_1_DGf.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_36_1_BKW.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_3_1_KJY.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_4_1_kpS.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_5_1_NAZ.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_6_1_0j4.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_7_1_mqU.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_8_1_Mbf.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_9_1_WIH.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_10_1_jhj.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_11_1_kNy.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_12_2_npw.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_13_1_X1B.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_14_2_QKQ.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_15_1_Gjd.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_16_1_dZO.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_17_1_GT9.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_18_1_LMC.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_19_1_uVr.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_1_1_kxN.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_20_1_F7a.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_21_1_nWa.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_22_1_s6a.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_23_1_pJk.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_24_1_3Wm.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_25_1_Ujc.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_26_1_nA0.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_27_1_slq.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_28_1_X0l.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_29_1_COE.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_2_1_WbC.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_30_1_DL8.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_31_1_I8W.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_32_1_AJw.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_33_1_IIU.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_34_2_Qg9.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_35_1_GVe.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_36_1_epv.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_37_1_wbp.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_38_1_uHp.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_39_2_xaU.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_3_1_a2o.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_40_1_PgW.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_4_1_uH5.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_5_1_cqc.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_6_1_bm5.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_7_1_e6U.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_8_1_fzg.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_9_1_SPk.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_10_1_UZx.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_11_1_4Sq.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_12_1_fC9.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_13_1_RLE.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_14_1_Hv3.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_15_1_oH6.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_16_1_I5y.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_17_1_u62.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_18_1_Ph0.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_19_1_55R.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_1_1_xsy.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_20_1_ADX.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_21_1_QpB.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_22_1_RMY.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_23_1_iye.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_24_1_idF.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_25_1_JkH.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_26_1_AeV.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_27_1_9Km.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_28_1_5Fn.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_29_1_rre.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_2_1_MZ4.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_30_1_3nR.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_31_1_Ngu.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_32_1_bVL.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_33_1_0X2.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_34_1_7qw.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_35_1_acT.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_36_1_6Sv.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_37_1_8Dv.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_38_1_j5Z.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_39_2_0Ui.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_3_1_Hbx.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_40_2_ziZ.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_41_1_lBv.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_42_1_OkS.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_43_1_NCP.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_4_1_E91.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_5_1_EcV.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_6_1_vMz.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_7_1_0mg.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_8_1_7ut.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_9_1_3g1.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_10_1_c83.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_11_1_iKL.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_12_1_X9n.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_13_1_WPz.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_14_1_8DG.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_15_1_5LX.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_16_1_4Ul.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_17_1_BZy.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_18_1_kMy.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_19_1_0SJ.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_1_1_CIZ.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_20_1_gjk.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_21_1_IpM.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_22_1_JDa.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_23_1_PC2.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_24_1_ve2.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_25_1_Pbu.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_26_1_xqg.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_27_1_Wy0.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_28_1_xOI.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_29_1_ip2.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_2_1_IRZ.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_30_1_r7s.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_31_1_L47.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_32_1_aRt.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_33_1_NGP.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_34_1_ZzX.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_35_1_fZy.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_36_1_4nE.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_37_1_zLM.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_38_1_W4N.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_39_1_d7v.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_3_1_5Zf.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_4_1_n0H.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_5_1_d6d.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_6_2_M5b.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_7_1_7o9.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_8_1_QEv.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_9_1_KiG.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_10_1_Sqr.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_11_1_K72.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_12_1_PmO.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_13_1_hF8.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_14_1_ULD.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_15_1_7IF.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_16_1_Jqu.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_17_1_Snf.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_18_1_TTY.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_19_1_79t.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_1_1_QTT.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_20_1_AZy.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_21_1_pFK.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_22_1_8sl.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_23_1_I4V.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_24_1_Dba.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_25_1_QyT.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_26_1_bJf.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_27_1_IID.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_28_2_zW4.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_29_1_oTq.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_2_1_RvA.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_30_1_mWW.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_31_1_5Sc.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_32_1_SNM.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_33_1_49F.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_34_1_rTp.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_35_1_eET.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_3_1_p33.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_4_1_Sft.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_5_1_CG6.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_6_1_F6P.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_7_1_Rlv.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_8_1_hsC.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_9_1_Ugj.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_10_1_A6n.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_11_1_S8F.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_12_1_gw9.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_13_1_aoP.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_14_1_NHr.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_15_1_z0g.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_16_1_FjU.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_17_2_1bn.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_18_1_8sW.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_19_1_NVd.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_1_1_MqY.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_20_1_IxG.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_21_1_g3p.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_22_1_5Et.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_23_1_h46.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_24_1_sLF.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_25_1_1IK.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_26_2_V7Z.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_27_2_BWc.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_28_1_Ycj.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_29_1_S2u.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_2_1_wwl.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_30_1_EWL.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_31_1_13X.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_32_1_PwA.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_3_1_IW6.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_4_2_NlB.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_5_1_QvM.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_6_2_USs.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_7_1_eAO.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_8_1_cmS.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_9_1_MLw.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_10_1_Fw5.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_11_1_D8d.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_12_2_hPU.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_13_1_g0Q.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_14_1_aOU.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_15_1_zK3.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_16_1_FfF.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_17_1_8bN.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_18_1_NrR.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_19_1_oGB.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_1_1_Brv.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_20_1_Rj7.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_21_1_AdF.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_22_1_jbP.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_23_1_RPG.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_24_1_9nP.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_25_1_HaD.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_26_1_EUc.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_27_1_kQb.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_28_1_04q.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_29_1_YRf.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_2_1_uIg.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_30_1_Yqf.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_31_1_nJ1.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_32_1_Zip.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_33_1_PFl.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_3_1_SHE.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_4_1_Jb8.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_5_1_7vc.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_6_1_oTl.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_7_1_wwF.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_8_1_I00.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_9_1_KFX.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_10_1_8eT.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_11_1_rce.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_12_1_2KS.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_13_1_Oed.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_14_1_TXw.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_15_1_SGl.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_16_1_rH9.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_17_1_CQO.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_1_1_aoX.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_2_1_5n2.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_3_1_Hln.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_4_1_iSR.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_5_1_ZP3.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_6_1_AiF.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_7_1_psu.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_8_1_Q29.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_9_1_xEY.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_10_1_0NJ.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_11_1_3Cs.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_12_1_t7q.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_13_1_xpr.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_14_1_qRQ.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_15_1_8FF.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_16_1_NyE.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_17_1_8Pa.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_18_1_nGg.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_19_1_x4V.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_1_1_anb.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_20_1_Sqf.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_2_1_n6L.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_3_1_bzq.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_4_1_r7A.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_5_1_H3c.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_6_1_c9T.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_7_1_ox2.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_8_1_zJi.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_9_1_KzN.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_10_1_wHJ.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_11_1_NnM.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_12_1_8wD.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_13_1_eOA.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_14_1_V0x.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_15_1_Ft7.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_16_1_EUK.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_17_1_sxW.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_1_1_xjb.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_2_1_HIP.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_3_1_L48.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_4_1_FAv.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_5_1_pVs.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_6_1_Bnm.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_7_1_Zq7.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_8_1_l1e.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_9_1_kec.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_10_1_TMv.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_11_1_lko.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_12_1_3jX.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_13_1_JRG.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_14_1_H4F.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_15_1_2HW.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_16_1_osc.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_17_1_xaD.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_18_1_BvQ.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_1_1_66b.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_2_1_0QY.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_3_1_s1O.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_4_1_yun.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_5_1_a0c.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_6_1_BVk.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_7_1_7eR.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_8_1_uBl.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_9_1_o2I.root'\n    ])" )
#"readFiles.extend([\n    ])\n"
#CleanJets output file
cleanJetsOutFiles=( "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-20to30.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-30to50.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-50to80.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-80to120.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-120to170.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-170to300.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-300to470.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-470to600.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-600to800.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-800to1000.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_QCD_Pt-1000.root" )

#TauAnalyzer output files
isoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-20to30_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-30to50_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-50to80_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-80to120_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-120to170_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-170to300_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-300to470_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-470to600_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-600to800_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-800to1000_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_QCD_Pt-1000_${version}.root" )
nonIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-20to30_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-30to50_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-50to80_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-80to120_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-120to170_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-170to300_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-300to470_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-470to600_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-600to800_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-800to1000_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_QCD_Pt-1000_${version}.root" )
nonIsoReweightTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-20to30_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-30to50_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-50to80_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-80to120_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-120to170_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-170to300_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-300to470_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-470to600_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-600to800_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-800to1000_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_QCD_Pt-1000_${version}.root" )
allTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-20to30_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-30to50_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-50to80_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-80to120_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-120to170_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-170to300_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-300to470_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-470to600_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-600to800_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-800to1000_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_QCD_Pt-1000_${version}.root" )

#EDM output files
EDMOutputFiles=( "${EDMOutputFilePrefix}QCD_Pt-20to30${infoTag}_${version}.root" "${EDMOutputFilePrefix}QCD_Pt-30to50${infoTag}_${version}.root" "${EDMOutputFilePrefix}QCD_Pt-50to80${infoTag}_${version}.root" "${EDMOutputFilePrefix}QCD_Pt-80to120${infoTag}_${version}.root" "${EDMOutputFilePrefix}QCD_Pt-120to170${infoTag}_${version}.root" "${EDMOutputFilePrefix}QCD_Pt-170to300${infoTag}_${version}.root" "${EDMOutputFilePrefix}QCD_Pt-300to470${infoTag}_${version}.root" "${EDMOutputFilePrefix}QCD_Pt-470to600${infoTag}_${version}.root" "${EDMOutputFilePrefix}QCD_Pt-600to800${infoTag}_${version}.root" "${EDMOutputFilePrefix}QCD_Pt-800to1000${infoTag}_${version}.root" "${EDMOutputFilePrefix}QCD_Pt-1000${infoTag}_${version}.root" )

#samples
samples=( "QCD_Pt-20to30" "QCD_Pt-30to50" "QCD_Pt-50to80" "QCD_Pt-80to120" "QCD_Pt-120to170" "QCD_Pt-170to300" "QCD_Pt-300to470" "QCD_Pt-470to600" "QCD_Pt-600to800" "QCD_Pt-800to1000" "QCD_Pt-1000" )

####GENERATION LOOP####

#change to working directory
mkdir -p $dir
cd $dir

#loop over number of samples
for i in `seq $iBeg $iEnd`
  do

  #generate cfg file for the isolated sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%NONISOTAUANALYZEROUTFILE%${nonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%ALLTAUANALYZEROUTFILE%${allTauAnalyzerOutputFiles[${i}]}%" -e "s%ISOTAUANALYZEROUTFILE%${isoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%SEQUENCE%process.isoTauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%REWEIGHT%False%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_iso_cfg.py

  #generate cfg file for the non-isolated sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%NONISOTAUANALYZEROUTFILE%${nonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%ALLTAUANALYZEROUTFILE%${allTauAnalyzerOutputFiles[${i}]}%" -e "s%ISOTAUANALYZEROUTFILE%${isoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%SEQUENCE%process.nonIsoTauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%REWEIGHT%False%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_nonIso_cfg.py

  #generate cfg file for the non-isolated, reweighted sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%NONISOTAUANALYZEROUTFILE%${nonIsoReweightTauAnalyzerOutputFiles[${i}]}%" -e "s%ALLTAUANALYZEROUTFILE%${allTauAnalyzerOutputFiles[${i}]}%" -e "s%ISOTAUANALYZEROUTFILE%${isoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%SEQUENCE%process.nonIsoTauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%REWEIGHT%True%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_nonIsoReweight_cfg.py

  #generate cfg file for the sample with no isolation cut
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%NONISOTAUANALYZEROUTFILE%${nonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%ALLTAUANALYZEROUTFILE%${allTauAnalyzerOutputFiles[${i}]}%" -e "s%ISOTAUANALYZEROUTFILE%${isoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%SEQUENCE%process.tauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%REWEIGHT%False%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_all_cfg.py

  #generate iso+nonIso+reweight job submission script for LSF
  #NOTE: the "echo" and "ls" commands in this CAT are all Kyle Tos's adding to figure out what is wrong with Condor running this program
  cat <<EOF > tauanalyzer_${samples[${i}]}_cfg.sh
#!/bin/bash
echo "Running tauanalyzer_${samples[${i}]}_cfg.sh"
jobDir="`pwd`"
fileNamePrefix="tauanalyzer_${samples[${i}]}"

cd \$jobDir
eval \`scramv1 runtime -sh\`
cd -
cp \$jobDir/\${fileNamePrefix}_iso_cfg.py \$jobDir/\${fileNamePrefix}_nonIso_cfg.py \$jobDir/\${fileNamePrefix}_nonIsoReweight_cfg.py .
echo "First copy done"
cmsRun \${fileNamePrefix}_iso_cfg.py > cmsRun_\${fileNamePrefix}_iso_cfg.out
echo "cmsRun fileName_iso_cfg.py DONE"
if [ $reweightOnly -eq 0 ]
    then
    echo "Just inside first if loop"
    cmsRun \${fileNamePrefix}_nonIso_cfg.py > cmsRun_\${fileNamePrefix}_nonIso_cfg.out
    echo "cmsRun \${fileNamePrefix}_nonIso_cfg.py DONE"
    echo "List of files to be copied in nonIsoTauAnalyzerOutputFiles in if statement: "
    ls -1 ${nonIsoTauAnalyzerOutputFiles[${i}]}
    cp -f ${nonIsoTauAnalyzerOutputFiles[${i}]} /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/
    rm ${nonIsoTauAnalyzerOutputFiles[${i}]}
    echo "Just copied to \$work and removed the files within the if statement"
fi
echo "End of if statement"
cmsRun \${fileNamePrefix}_nonIsoReweight_cfg.py > cmsRun_\${fileNamePrefix}_nonIsoReweight_cfg.out
echo "cmsRun \${fileNamePrefix}_nonIsoReweight_cfg.py DONE"
echo "List of files to be copied in isoTauAnalyzerOutputFiles: "
ls -1 ${isoTauAnalyzerOutputFiles[${i}]}
cp -f ${isoTauAnalyzerOutputFiles[${i}]} /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/
echo "List of files to be copied in nonIsoReweightTauAnalyzerOutputFiles: "
ls -1 ${nonIsoReweightTauAnalyzerOutputFiles[${i}]}
cp -f ${nonIsoReweightTauAnalyzerOutputFiles[${i}]} /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/
rm ${isoTauAnalyzerOutputFiles[${i}]} ${nonIsoReweightTauAnalyzerOutputFiles[${i}]}
echo "Removed both of the copied files"
exit 0
EOF
  chmod a+x tauanalyzer_${samples[${i}]}_cfg.sh

  #generate noIsoCut job submission script for LSF
  #NOTE: the "echo" and "ls" commands in this CAT are all Kyle Tos's adding to figure out what is wrong with Condor running this program
  cat <<EOF > tauanalyzer_${samples[${i}]}_all_cfg.sh
#!/bin/bash
echo "Running tauanalyzer_${samples[${i}]}_all_cfg.sh"
jobDir="`pwd`"
fileNamePrefix="tauanalyzer_${samples[${i}]}"

cd \$jobDir
eval \`scramv1 runtime -sh\`
cd -
cp \$jobDir/\${fileNamePrefix}_all_cfg.py .
echo "First copy DONE"
cmsRun \${fileNamePrefix}_all_cfg.py > cmsRun_\${fileNamePrefix}_all_cfg.out
echo "cmsRun \${fileNamePrefix}_all_cfg.py DONE"
echo "List of the files in {allTauAnalyzerOutputFiles[${i}]} to be copied: "
ls -1 ${allTauAnalyzerOutputFiles[${i}]}
cp -f ${allTauAnalyzerOutputFiles[${i}]} /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/
rm ${allTauAnalyzerOutputFiles[${i}]}
echo "Removing DONE and file execution DONE"
exit 0
EOF
  chmod a+x tauanalyzer_${samples[${i}]}_all_cfg.sh
done

#generate run cfg that runs all files in the directory
cat <<EOF > runQCDTauAnalyzerCfgs.sh
#!/bin/bash

for file in \`ls -alh *QCD_*.py | awk '{ print \$9 }'\`
  do
  outFile=\`echo \$file | sed -e "s%\.py%.txt%"\`
  cmsRun \$file > \$outFile
done

exit 0
EOF
chmod a+x runQCDTauAnalyzerCfgs.sh

#generate script that submits all iso+nonIso+reweight jobs to LSF
cat <<EOF > submitQCDTauAnalyzerJobs.sh
#!/bin/bash

for file in \`ls -alh tauanalyzer*QCD_*.sh | grep -v all | awk '{ print \$9 }'\`
  do
  jobName=\`echo \$file | sed -e "s%\(.*\)\.sh%\1%"\`
  echo "\$file"

  cat>Csubmit_\$jobName<<EOF
Universe   = vanilla
Executable = \$file
Log        = Csubmit_\$jobName.log
Output     = Csubmit_\$jobName.out
Queue
EOF

echo "EOF

echo \"generateQCDTauAnalyzerCfgs.sh\"
condor_submit  Csubmit_\$jobName
done
exit 0" >> submitQCDTauAnalyzerJobs.sh
chmod a+x submitQCDTauAnalyzerJobs.sh

#generate script that submits all noIsoCut jobs to LSF
cat <<EOF > submitQCDAllTauAnalyzerJobs.sh
#!/bin/bash

for file in \`ls -alh tauanalyzer*QCD_*all*.sh | awk '{ print \$9 }'\`
  do
  jobName=\`echo \$file | sed -e "s%\(.*\)\.sh%\1%"\`
  echo "\$file"

  cat>Csubmit_\$jobName<<EOF
Universe   = vanilla
Executable = \$file
Log        = Csubmit_\$jobName.log
Output     = Csubmit_\$jobName.out
Queue
EOF

echo "EOF

echo \"generateQCDTauAnalyzerCfgs.sh\"
condor_submit  Csubmit_\$jobName
done
exit 0" >> submitQCDTauAnalyzerJobs.sh
chmod a+x submitQCDAllTauAnalyzerJobs.sh

#generate script that copies all iso+nonIso+reweight files locally from EOS
cat <<EOF > copyQCDFromEOS.sh
#!/bin/bash

eval \`scramv1 runtime -sh\`
for sample in "20to30" "30to50" "50to80" "80to120" "120to170" "170to300" "300to470" "470to600" "600to800" "800to1000" "1000"
  do
  for cut in Iso NonIso NonIsoReweight
    do
    if [ "\$cut" != "NonIso" ] || [ $reweightOnly -eq 0 ]
        then
        cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/muHad\${cut}Analysis_QCD_Pt-\${sample}_${version}.root /mnt/hadoop/store/user/kmtos/data1/`whoami`/QCD/analysis/
        rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/muHad\${cut}Analysis_QCD_Pt-\${sample}_${version}.root
    fi
  done
done

exit 0
EOF
chmod a+x copyQCDFromEOS.sh

#generate script that copies all noIsoCut files locally from EOS
cat <<EOF > copyAllQCDFromEOS.sh
#!/bin/bash

eval \`scramv1 runtime -sh\`
for sample in "20to30" "30to50" "50to80" "80to120" "120to170" "170to300" "300to470" "470to600" "600to800" "800to1000" "1000"
  do
  cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/muHadAnalysis_QCD_Pt-\${sample}_${version}.root /mnt/hadoop/store/user/kmtos/data1/`whoami`/QCD/analysis/
  rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/muHadAnalysis_QCD_Pt-\${sample}_${version}.root
done
exit 0
EOF
chmod a+x copyAllQCDFromEOS.sh

exit 0
