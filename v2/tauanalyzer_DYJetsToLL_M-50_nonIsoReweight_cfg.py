import FWCore.ParameterSet.Config as cms

process = cms.Process("MUHADANALYSIS")

#PDG IDs
A_PDGID = 36
Z_PDGID = 23
W_PDGID = 24
TAU_PDGID = 15
MU_PDGID = 13
NUMU_PDGID = 14
NUTAU_PDGID = 16
D_PDGID = 1
U_PDGID = 2
S_PDGID = 3
C_PDGID = 4
B_PDGID = 5
T_PDGID = 6
G_PDGID = 21
ANY_PDGID = 0

#tau decay types
TAU_HAD = 0
TAU_MU = 1
TAU_E = 2
TAU_ALL = 3

#tau hadronic decay types
TAU_ALL_HAD = -1
TAU_1PRONG_0NEUTRAL = 0
TAU_1PRONG_1NEUTRAL = 1
TAU_1PRONG_2NEUTRAL = 2
TAU_1PRONG_3NEUTRAL = 3
TAU_1PRONG_NNEUTRAL = 4
TAU_2PRONG_0NEUTRAL = 5
TAU_2PRONG_1NEUTRAL = 6
TAU_2PRONG_2NEUTRAL = 7
TAU_2PRONG_3NEUTRAL = 8
TAU_2PRONG_NNEUTRAL = 9
TAU_3PRONG_0NEUTRAL = 10
TAU_3PRONG_1NEUTRAL = 11
TAU_3PRONG_2NEUTRAL = 12
TAU_3PRONG_3NEUTRAL = 13
TAU_3PRONG_NNEUTRAL = 14
TAU_RARE = 15

#no consideration of pT rank
ANY_PT_RANK = -1

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)
#process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1)

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

readFiles = cms.untracked.vstring()
process.source = cms.Source(
    "PoolSource",
    fileNames = readFiles,
    skipEvents = cms.untracked.uint32(0)
    )
readFiles.extend([
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_100_1_Csf.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_101_1_J24.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_102_1_BUw.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_103_1_z8y.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_104_1_hDx.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_105_1_4q2.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_106_1_usU.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_107_1_kwp.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_108_1_zin.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_109_1_xo8.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_10_1_v4l.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_110_1_7IT.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_111_1_fRI.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_112_1_T3P.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_113_1_qb2.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_114_1_wdy.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_115_1_5q6.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_116_1_zvA.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_117_1_eU3.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_118_1_QFr.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_119_1_uPo.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_11_1_b5g.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_120_1_n6u.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_121_1_Ppb.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_122_1_zEw.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_123_1_dJJ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_124_1_c49.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_125_1_PUV.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_126_1_Uw0.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_127_1_EMW.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_128_1_Smw.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_129_1_V2T.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_12_1_k0o.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_130_1_Z1R.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_131_2_JNE.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_132_1_0Ox.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_133_1_Fvb.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_134_1_sgl.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_135_1_J54.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_136_2_RlS.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_137_1_Muj.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_138_2_1s3.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_139_2_Sp9.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_13_1_aIa.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_140_1_D7q.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_141_2_WRV.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_142_2_LMj.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_143_1_BMb.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_144_1_45r.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_145_2_DH3.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_146_1_o0h.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_147_1_nMh.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_148_2_BX3.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_149_1_U9C.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_14_2_GrH.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_150_1_DjG.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_151_2_QHo.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_152_2_1Le.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_153_2_jty.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_154_2_vhP.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_155_2_V7n.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_156_2_lIk.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_157_2_8r5.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_158_2_ILn.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_159_1_Rzf.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_15_1_bL7.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_160_2_gKo.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_161_1_5Na.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_162_2_1Hr.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_163_1_Gtq.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_164_2_HKT.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_165_2_nPK.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_166_2_i1c.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_167_1_jtB.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_168_1_Eyl.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_169_1_JlD.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_16_1_ZAQ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_170_1_O1Y.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_171_1_Qgn.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_172_1_DaL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_173_1_yXh.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_174_1_cwW.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_175_1_UHL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_176_1_2F9.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_177_1_Vzy.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_178_1_w4V.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_179_1_YZo.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_17_1_s6z.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_180_1_HFx.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_181_1_mPk.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_182_1_89l.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_183_1_5EL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_184_1_FkX.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_185_1_NLz.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_186_1_gPD.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_187_1_Zto.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_188_1_Fuf.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_189_1_6Bv.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_18_1_lOH.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_190_1_QdJ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_191_2_vfV.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_192_2_yq4.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_193_2_LMm.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_194_1_GdT.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_195_2_AKl.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_196_2_6ZP.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_197_1_tNT.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_198_1_j0G.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_199_2_MyX.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_19_1_eco.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_1_1_qTf.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_200_2_FS2.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_201_2_VPD.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_202_2_Ll7.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_203_2_quL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_204_2_r4b.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_205_2_JsN.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_206_2_BOu.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_207_2_W04.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_208_2_tuW.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_209_1_7Wb.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_20_1_hIX.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_210_1_aaC.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_211_1_B2r.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_212_2_esT.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_213_2_VD8.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_214_1_RW2.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_215_1_PNj.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_216_1_5ma.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_217_1_N9Y.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_218_1_tGb.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_219_1_CyF.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_21_1_o3B.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_220_1_m7R.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_221_1_X3d.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_222_1_1X2.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_223_1_CZY.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_224_1_nL3.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_225_1_HtQ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_226_1_ln8.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_227_1_LYp.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_228_1_nMa.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_229_1_RTs.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_22_2_KrR.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_230_1_8d0.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_231_1_RzL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_232_1_mWT.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_233_1_faY.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_234_1_tpq.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_235_1_zGL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_236_1_bOx.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_237_1_V8C.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_238_1_Blg.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_239_1_JCQ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_23_1_m7Y.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_240_1_L2c.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_241_1_ul6.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_242_1_VOL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_243_1_VjZ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_244_1_qk3.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_245_1_kzE.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_246_1_zgh.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_247_1_9Sd.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_248_1_Qne.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_249_1_wCg.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_24_1_qXX.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_250_1_uC4.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_251_1_7rs.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_252_1_sOW.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_253_1_s5U.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_254_1_W2g.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_255_1_If9.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_256_1_Tfz.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_257_1_Rr7.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_258_1_9yb.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_259_1_znl.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_25_1_tTy.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_260_1_tFw.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_261_1_3aj.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_262_2_9Ux.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_263_1_gwf.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_264_1_94i.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_265_1_dRW.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_266_1_AdD.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_267_1_s6z.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_268_1_lRr.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_269_1_RvK.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_26_1_SAB.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_270_1_c7T.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_271_1_yJU.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_272_1_uhN.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_273_1_NCa.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_274_1_7T0.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_275_1_Ds1.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_276_1_VjS.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_277_1_7jT.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_278_1_hza.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_279_1_uKb.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_27_1_0ui.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_280_1_G3w.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_281_1_uY1.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_282_1_zD7.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_283_1_EM2.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_284_1_rMy.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_285_1_gh1.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_286_1_JeH.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_287_1_6QP.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_288_1_fUL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_289_1_3oH.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_28_1_IHG.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_290_1_uCY.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_291_2_p6C.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_292_2_2IK.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_293_1_j6g.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_294_1_NNq.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_295_1_OW1.root'
    ])
readFiles.extend([
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_296_2_muk.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_297_2_IIX.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_298_2_rqS.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_299_1_KFg.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_29_1_ldx.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_2_1_wIP.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_300_2_8CX.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_301_2_iiV.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_302_2_3gl.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_303_2_ZFp.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_304_2_JUu.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_305_2_rqO.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_306_2_VKj.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_307_1_Jfi.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_308_2_psS.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_309_1_wMg.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_30_1_qHP.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_31_1_5AR.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_32_1_xHp.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_33_1_AvT.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_34_1_gYq.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_35_1_Fd1.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_36_1_QzZ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_37_1_BoV.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_38_1_fX4.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_39_1_iMQ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_3_1_WdR.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_40_1_Q7K.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_41_1_7vA.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_42_1_Fqf.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_43_1_mts.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_44_1_gMU.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_45_1_52f.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_46_1_nUc.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_47_1_c6s.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_48_1_WKY.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_49_1_p0t.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_4_1_lGZ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_50_1_Un6.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_51_1_XgZ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_52_1_bmi.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_53_1_1XP.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_54_1_RFv.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_55_1_M2c.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_56_1_evx.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_57_1_GFl.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_58_1_dbp.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_59_1_EPK.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_5_1_qg1.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_60_1_slF.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_61_1_2eQ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_62_1_PXO.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_63_1_JhZ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_64_1_gnW.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_65_1_EXB.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_66_1_uLO.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_67_1_2OY.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_68_1_9hN.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_69_1_vi6.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_6_1_Ete.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_70_1_Qax.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_71_1_p96.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_72_1_252.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_73_1_3mA.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_74_1_D3u.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_75_1_6Gp.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_76_1_2I3.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_77_1_BLm.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_78_1_eE9.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_79_1_XwD.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_7_1_DpY.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_80_1_XqT.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_81_1_Fbg.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_82_1_D6R.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_83_1_2NZ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_84_1_yUb.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_85_1_IAZ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_86_1_jUv.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_87_1_cD3.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_88_1_Yd7.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_89_1_ys8.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_8_1_XkG.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_90_1_Z0G.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_91_1_5Qs.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_92_1_BOO.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_93_1_TQw.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_94_1_KIo.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_95_1_anB.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_96_1_pMG.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_97_1_s7K.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_98_1_mri.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_99_1_7Tm.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/data_no_selection_9_1_dS9.root'
    ])

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck') #speed?

#for L1GtStableParametersRcd and jet corrections
#START52_V9B is recommended for JEC in Summer12 CMSSWv5.2 MC
#START52_V9 is what the Summer12 CMSSWv5.2 MC was produced with
#START53_V15 is the latest recommended JEC tag
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('START53_V15::All')

#for HLT selection
process.load('HLTrigger/HLTfilters/hltHighLevel_cfi')

#for mu-less jets
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")
process.load("RecoTauTag.RecoTau.RecoTauPiZeroProducer_cfi")
process.load('BoostedTauAnalysis/CleanJets/cleanjets_cfi')
process.load('BoostedTauAnalysis/TauAnalyzer/tauanalyzer_cfi')
process.load('JetMETCorrections.Type1MET.pfMETCorrections_cff')

## #for jet charged hadron subtraction
## process.load("CommonTools.ParticleFlow.PF2PAT_cff")
## from CommonTools.ParticleFlow.Tools.enablePileUpCorrection import enablePileUpCorrectionInPF2PAT
## # the following is advocated by JetMET, but leads to include very far tracks in the no pile up collection
## # enablePileUpCorrectionInPF2PAT( process, postfix='')

#for jet corrections
process.load('JetMETCorrections.Configuration.JetCorrectionServices_cff')

# b-tagging general configuration
process.load("RecoBTag.Configuration.RecoBTag_cff")
process.load("RecoJets.JetAssociationProducers.ak5JTA_cff")
from RecoBTag.SoftLepton.softLepton_cff import *
from RecoBTag.ImpactParameter.impactParameter_cff import *
from RecoBTag.SecondaryVertex.secondaryVertex_cff import *
from RecoBTau.JetTagComputer.combinedMVA_cff import *
process.impactParameterTagInfos.jetTracks = cms.InputTag("ak5JetTracksAssociatorAtVertex")
process.ak5JetTracksAssociatorAtVertex.jets = cms.InputTag("ak5PFJets")
process.ak5JetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
process.btagging = cms.Sequence(
    process.ak5JetTracksAssociatorAtVertex*
    # impact parameters and IP-only algorithms
    process.impactParameterTagInfos*
    (process.trackCountingHighEffBJetTags +
     process.trackCountingHighPurBJetTags +
     process.jetProbabilityBJetTags +
     process.jetBProbabilityBJetTags +
     # SV tag infos depending on IP tag infos, and SV (+IP) based algos
     process.secondaryVertexTagInfos*
     (process.simpleSecondaryVertexHighEffBJetTags +
      process.simpleSecondaryVertexHighPurBJetTags +
      process.combinedSecondaryVertexBJetTags +
      process.combinedSecondaryVertexMVABJetTags) +
     process.ghostTrackVertexTagInfos*
     process.ghostTrackBJetTags)##  +
##     process.softPFMuonsTagInfos*
##     process.softPFMuonBJetTags *
##     process.softPFElectronsTagInfos*
##     process.softPFElectronBJetTags
    )

#define a parameter set to be passed to all modules that utilize GenTauDecayID for signal taus
commonGenTauDecayIDPSet = cms.PSet(momPDGID = cms.vint32(A_PDGID),
                                   chargedHadronPTMin = cms.double(0.0),
                                   neutralHadronPTMin = cms.double(0.0),
                                   chargedLeptonPTMin = cms.double(0.0),
                                   totalPTMin = cms.double(0.0))

#define a parameter set for the W-->munu selector
WMuNuPSet = commonGenTauDecayIDPSet.clone()
WMuNuPSet.momPDGID = cms.vint32(W_PDGID)

#only proceed if event is a true W-->munu event
process.genWMuNuSelector = cms.EDFilter(
    'GenObjectProducer',
    genParticleTag = cms.InputTag('genParticles'),
    absMatchPDGIDs = cms.vuint32(MU_PDGID),
    sisterAbsMatchPDGID = cms.uint32(NUMU_PDGID),
    genTauDecayIDPSet = WMuNuPSet,
    primaryTauDecayType = cms.uint32(TAU_ALL),
    sisterTauDecayType = cms.uint32(TAU_ALL),
    primaryTauPTRank = cms.int32(ANY_PT_RANK),
    primaryTauHadronicDecayType = cms.int32(TAU_ALL_HAD),
    sisterHadronicDecayType = cms.int32(TAU_ALL_HAD),
    primaryTauAbsEtaMax = cms.double(-1.0),
    primaryTauPTMin = cms.double(-1.0),
    countSister = cms.bool(False),
    applyPTCuts = cms.bool(False),
    countKShort = cms.bool(True),
    minNumGenObjectsToPassFilter = cms.uint32(0),
    makeAllCollections = cms.bool(False)
    )

#produce a collection of muons from W-->tau(-->mu)nu
process.genWTauNuSelector = process.genWMuNuSelector.clone()
process.genWTauNuSelector.absMatchPDGIDs = cms.vuint32(TAU_PDGID)
process.genWTauNuSelector.sisterAbsMatchPDGID = cms.uint32(NUTAU_PDGID)
process.genWTauNuSelector.primaryTauDecayType = cms.uint32(TAU_MU)

#require event to fire IsoMu24_eta2p1
process.IsoMu24eta2p1Selector = process.hltHighLevel.clone()
process.IsoMu24eta2p1Selector.HLTPaths = cms.vstring('HLT_IsoMu24_eta2p1_v11')

#search for a muon with pT > 25 GeV as in WHbb CMS AN-2012/349 and proceed if one can be found
#this will produce a ref to the original muon collection
process.WMuonPTSelector = cms.EDFilter('MuonRefSelector',
                                       src = cms.InputTag('muons'),
                                       cut = cms.string('pt > 25.0'),
                                       filter = cms.bool(True)
                                       )

#search for a loose PF isolated tight muon in |eta| < 2.1 with pT > 25 GeV
#(see https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Muon_Isolation_AN1 for
#isolation definition;CMS AN-2012/349 uses loose isolation working point for WHbb muon selection)
#this will produce a ref to the original muon collection
process.WIsoMuonSelector = cms.EDFilter('CustomMuonSelector',
                                        baseMuonTag = cms.InputTag('muons'),
                                        muonTag = cms.InputTag('WMuonPTSelector'),
                                        vtxTag = cms.InputTag('offlinePrimaryVertices'),
                                        muonID = cms.string('tight'),
                                        PFIsoMax = cms.double(0.2),
                                        detectorIsoMax = cms.double(-1.0),
                                        PUSubtractionCoeff = cms.double(0.5),
                                        usePFIso = cms.bool(True),
                                        passIso = cms.bool(True),
                                        etaMax = cms.double(2.1),
                                        minNumObjsToPassFilter = cms.uint32(1)
                                        )

#search for a muon with pT > 5 GeV as in HZZ4l analysis and proceed if one can be found
#this will produce a ref to the original muon collection
process.tauMuonPTSelector = cms.EDFilter('MuonRefSelector',
                                         src = cms.InputTag('muons'),
                                         cut = cms.string('pt > 5.0'),
                                         filter = cms.bool(True)
                                         )

#search for soft muons
#(see https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Soft_Muon) not overlapping with
#the W muon in |eta| < 2.4
#this will produce a ref to the original muon collection
process.tauMuonSelector = cms.EDFilter('CustomMuonSelector',
                                       baseMuonTag = cms.InputTag('muons'),
                                       muonTag = cms.InputTag('tauMuonPTSelector'),
                                       vtxTag = cms.InputTag('offlinePrimaryVertices'),
                                       vetoMuonTag = cms.InputTag('WIsoMuonSelector'),
                                       muonID = cms.string('soft'),
                                       PFIsoMax = cms.double(0.2),
                                       detectorIsoMax = cms.double(-1.0),
                                       PUSubtractionCoeff = cms.double(0.5),
                                       usePFIso = cms.bool(True),
                                       passIso = cms.bool(True),
                                       etaMax = cms.double(2.4),
                                       minNumObjsToPassFilter = cms.uint32(1)
                                       )

#produce gen parton collection
process.genPartonSelector = cms.EDFilter(
    'GenPartonProducer',
    genParticleTag = cms.InputTag('genParticles'),
    partonAbsEtaMax = cms.double(-1.0),
    partonPTMin = cms.double(-1.0),
    minNumGenObjectsToPassFilter = cms.uint32(0)
    )

#produce gen muon collection
process.genMuSelector = cms.EDFilter('PdgIdCandViewSelector',
                                     src = cms.InputTag('genParticles'),
                                     pdgId = cms.vint32(-13, 13))

#produce collection of gen muons from a1-->tau(-->mu)tau(-->had) decay
process.genTauMuSelector = cms.EDFilter(
    'GenObjectProducer',
    genParticleTag = cms.InputTag('genParticles'),
    absMatchPDGIDs = cms.vuint32(TAU_PDGID),
    sisterAbsMatchPDGID = cms.uint32(TAU_PDGID),
    genTauDecayIDPSet = commonGenTauDecayIDPSet,
    primaryTauDecayType = cms.uint32(TAU_MU),
    sisterTauDecayType = cms.uint32(TAU_HAD),
    primaryTauPTRank = cms.int32(ANY_PT_RANK),
    primaryTauHadronicDecayType = cms.int32(TAU_ALL_HAD),
    sisterHadronicDecayType = cms.int32(TAU_ALL_HAD),
    primaryTauAbsEtaMax = cms.double(-1.0),
    primaryTauPTMin = cms.double(-1.0),
    countSister = cms.bool(False),
    applyPTCuts = cms.bool(False),
    countKShort = cms.bool(True),
    minNumGenObjectsToPassFilter = cms.uint32(0),
    makeAllCollections = cms.bool(False)
    )

#clean the jets of soft muons, then rebuild the taus
process.CleanJets.muonSrc = cms.InputTag('tauMuonSelector')
process.CleanJets.PFCandSrc = cms.InputTag('particleFlow')
process.CleanJets.cutOnGenMatches = cms.bool(False)
process.CleanJets.outFileName = cms.string(
    'file://home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/NMSSMSignal_MuProperties_DYJetsToLL_M-50.root'
    )
process.recoTauAK5PFJets08Region.src = cms.InputTag("CleanJets", "ak5PFJetsNoMu",
                                                    "MUHADANALYSIS")
process.recoTauAK5PFJets08Region.jetMuonMapTag = cms.InputTag("CleanJets", "", "MUHADANALYSIS")
process.ak5PFJetsRecoTauPiZeros.jetSrc = cms.InputTag("CleanJets", "ak5PFJetsNoMu",
                                                      "MUHADANALYSIS")
process.combinatoricRecoTaus.jetSrc = cms.InputTag("CleanJets", "ak5PFJetsNoMu", "MUHADANALYSIS")
process.ak5PFJetTracksAssociatorAtVertex.jets = cms.InputTag("CleanJets", "ak5PFJetsNoMu",
                                                             "MUHADANALYSIS")
process.ak5PFJetsLegacyHPSPiZeros.jetSrc = cms.InputTag("CleanJets", "ak5PFJetsNoMu",
                                                        "MUHADANALYSIS")
process.recoTauCommonSequence = cms.Sequence(process.CleanJets*
                                             process.ak5PFJetTracksAssociatorAtVertex*
                                             process.recoTauAK5PFJets08Region*
                                             process.recoTauPileUpVertices*
                                             process.pfRecoTauTagInfoProducer
                                             )
process.PFTau = cms.Sequence(process.recoTauCommonSequence*process.recoTauClassicHPSSequence)

#produce a ref vector of taus that correspond to the up-shifted taus
process.originalUpShiftedTauProducer = cms.EDProducer(
    'ValueMapTauRefProducer',
    valMapTag = cms.InputTag('tauShiftProducer', 'hpsTausUpShifted', 'SKIM'),
    keyTag = cms.InputTag('tauShiftProducer', 'hpsTausUpShifted', 'SKIM')
    )

#produce a ref vector of taus that correspond to the down-shifted taus
process.originalDownShiftedTauProducer = cms.EDProducer(
    'ValueMapTauRefProducer',
    valMapTag = cms.InputTag('tauShiftProducer', 'hpsTausDownShifted', 'SKIM'),
    keyTag = cms.InputTag('tauShiftProducer', 'hpsTausDownShifted', 'SKIM')
    )

#find taus in |eta| < 2.4 matched to muon-tagged cleaned jets that pass the isolation
#discriminator
#this will produce a ref to the cleaned tau collection
process.muHadIsoTauSelector = cms.EDFilter(
    'CustomTauSepFromMuonSelector',
    tauTag = cms.InputTag('muHadTauSelector', '', 'SKIM'),
    baseTauTag = cms.InputTag('hpsPFTauProducer', '', 'SKIM'),
    tauHadIsoTag = cms.InputTag('hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr', '',
                                'SKIM'),
    tauDiscriminatorTags = cms.VInputTag(
    cms.InputTag('hpsPFTauDiscriminationByDecayModeFinding', '', 'SKIM'), 
    cms.InputTag('hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr', '', 'SKIM')
    ),
    jetTag = cms.InputTag('CleanJets', 'ak5PFJetsNoMu', 'SKIM'),
    muonRemovalDecisionTag = cms.InputTag('CleanJets', '', 'SKIM'),
    overlapCandTag = cms.InputTag('WIsoMuonSelector'),
    passDiscriminator = cms.bool(True),
    pTMin = cms.double(10.0),
    etaMax = cms.double(2.4),
    isoMax = cms.double(-1.0),
    dR = cms.double(0.5),
    minNumObjsToPassFilter = cms.uint32(1)
    )

#find taus in |eta| < 2.4 matched to muon-tagged cleaned jets that pass decay mode finding
#this will produce a ref to the cleaned tau collection
process.muHadTauSelector = process.muHadIsoTauSelector.clone()
process.muHadTauSelector.tauDiscriminatorTags = cms.VInputTag(
    cms.InputTag('hpsPFTauDiscriminationByDecayModeFinding', '', 'SKIM')
    )

#find taus in |eta| < 2.4 matched to muon-tagged cleaned jets that fail the isolation
#discriminator
#this will produce a ref to the cleaned tau collection
process.muHadNonIsoTauSelector = process.muHadIsoTauSelector.clone()
process.muHadNonIsoTauSelector.tauDiscriminatorTags = cms.VInputTag(
    cms.InputTag('hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr', '', 'SKIM')
    )
process.muHadNonIsoTauSelector.passDiscriminator = cms.bool(False)
process.muHadNonIsoTauSelector.isoMax = cms.double(5.0) #GeV

#produce AK5PFchs L1FastL2L3 corrected jets

#b-tag filter
process.IsoBVetoFilter = cms.EDFilter(
    'BVetoFilter',
    tauTag = cms.InputTag('muHadIsoTauSelector'),
    oldJetTag = cms.InputTag('ak5PFJets'),
    jetMuonMapTag = cms.InputTag('CleanJets', '', 'SKIM'),
    bTagInfoTag = cms.InputTag('combinedSecondaryVertexBJetTags'),
    CSVMax = cms.double(0.679),
    passFilter = cms.bool(True),
    minNumObjsToPassFilter = cms.uint32(1)
    )
process.NonIsoBVetoFilter = process.IsoBVetoFilter.clone()
process.NonIsoBVetoFilter.tauTag = cms.InputTag('muHadNonIsoTauSelector')
process.AllBVetoFilter = process.IsoBVetoFilter.clone()
process.AllBVetoFilter.tauTag = cms.InputTag('muHadTauSelector')

#create a collection of corrected jets with pT > 20 GeV and |eta| < 2.4 distinct from the W muon
#and isolated tau
#this collection has no memory of the uncorrected jets
process.corrJetDistinctIsoTauSelector = cms.EDFilter(
    'CustomJetSelector',
    tauTag = cms.InputTag('IsoBVetoFilter'),
    overlapCandTag = cms.InputTag('WIsoMuonSelector'),
    oldJetTag = cms.InputTag('ak5PFJets'),
    jetMuonMapTag = cms.InputTag('CleanJets'),
    pTMin = cms.double(30.0),
    absEtaMax = cms.double(2.4),
    dR = cms.double(0.3),
    minNumObjsToPassFilter = cms.uint32(0),
    maxNumObjsToPassFilter = cms.int32(-1)
    )

#create a collection of corrected jets with pT > 20 GeV and |eta| < 2.4 distinct from the W muon
#and non-isolated tau
#this collection has no memory of the uncorrected jets
process.corrJetDistinctNonIsoTauSelector = process.corrJetDistinctIsoTauSelector.clone()
process.corrJetDistinctNonIsoTauSelector.tauTag = cms.InputTag('NonIsoBVetoFilter')

#create a collection of corrected jets with pT > 20 GeV and |eta| < 2.4 distinct from the W muon
#and tau passing decay mode finding
#this collection has no memory of the uncorrected jets
process.corrJetDistinctTauSelector = process.corrJetDistinctIsoTauSelector.clone()
process.corrJetDistinctTauSelector.tauTag = cms.InputTag('AllBVetoFilter', '', 'MUHADANALYSIS')

#produce Type-1 corrected PFMET objects
process.pfMetType1 = process.pfType1CorrectedMet.clone()

process.producePFMETCorrections = cms.Sequence(
    process.pfCandsNotInJet
   * process.pfJetMETcorr
   * process.pfCandMETcorr
   * process.pfchsMETcorr
   * process.pfMetType1
)

#analyze isolated taus
process.highMTMuHadIsoTauAnalyzer = cms.EDAnalyzer(
    'TauAnalyzer',
    outFileName = cms.string(
    'file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadIsoAnalysis_highMT_DYJetsToLL_M-50_v2.root'
    ),
    tauTag = cms.InputTag('IsoBVetoFilter'),
    METTag = cms.InputTag('patType1CorrectedPFMetPFlow'),
    muonTag = cms.InputTag('WIsoMuonSelector'),
    muonPFIsoPUSubtractionCoeff = cms.double(0.5),
    genMatchedMuonTag = cms.InputTag('WIsoMuonSelector'),
    oldJetTag = cms.InputTag('ak5PFJets'),
    newJetTag = cms.InputTag('CleanJets', 'ak5PFJetsNoMu', 'SKIM'),
    jetMuonMapTag = cms.InputTag('CleanJets', '', 'SKIM'),
    oldNewJetMapTag = cms.InputTag('CleanJets', '', 'SKIM'),
    genParticleTag = cms.InputTag('genWMuNuSelector'),
    genTauMuTag = cms.InputTag('genTauMuSelector'),
    genWTauMuTag = cms.InputTag('genWTauNuSelector'),
    tauHadIsoTag = cms.InputTag('hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr', '',
                                'SKIM'),
    allMuonTag = cms.InputTag('muons'),
    muonGenParticleTag = cms.InputTag('genMuSelector'),
    PUTag = cms.InputTag('addPileupInfo'),
    vtxTag = cms.InputTag('offlinePrimaryVertices'),
    allGenParticleTag = cms.InputTag('genParticles'),
    corrJetTag = cms.InputTag('corrJetDistinctIsoTauSelector'),
    bJetTag = cms.InputTag('combinedSecondaryVertexBJetTags'),
    dR = cms.double(0.3),
    tauPTMin = cms.double(10.0), #GeV
    tauDecayMode = cms.int32(TAU_ALL_HAD),
    uncorrJetPTMin = cms.double(0.0), #GeV
    tauArbitrationMethod = cms.string("m"),
    PUScenario = cms.string("S10"),
    zCut = cms.double(0.1),
    RcutFactor = cms.double(0.5),
    CSVMax = cms.double(0.679),
    MC = cms.bool(True),
    reweight = cms.bool(False),
    bTagScaleShift = cms.string("mean"),
    sample = cms.string(""),
    pTRankColors = cms.vuint32(1, 2, 4, 6),
    pTRankStyles = cms.vuint32(20, 21, 22, 23),
    pTRankEntries = cms.vstring('Highest p_{T}', 'Second highest p_{T}', 'Third highest p_{T}',
                                'Lowest p_{T}'),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_IsoMu24_eta2p1_v1", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v2", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v3", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v4", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v5", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v6", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v7", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v8", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v9", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v10", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v11", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v12", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v13", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v14", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v15", "", "HLT")
                            ),
    theRightHLTTag = cms.InputTag("HLT_IsoMu24_eta2p1"),
    theRightHLTSubFilter = cms.InputTag("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3cr"),
    HLTSubFilters = cms.untracked.VInputTag("")
    )
process.lowMTMuHadIsoTauAnalyzer = process.highMTMuHadIsoTauAnalyzer.clone()
process.lowMTMuHadIsoTauAnalyzer.outFileName = cms.string('file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadIsoAnalysis_lowMT_DYJetsToLL_M-50_v2.root')

#analyze non-isolated taus
process.highMTMuHadNonIsoTauAnalyzer = process.highMTMuHadIsoTauAnalyzer.clone()
process.highMTMuHadNonIsoTauAnalyzer.outFileName = cms.string(
    'file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadNonIsoReweightAnalysis_DYJetsToLL_M-50_v2.root'
    )
process.highMTMuHadNonIsoTauAnalyzer.tauTag = cms.InputTag('NonIsoBVetoFilter')
process.highMTMuHadNonIsoTauAnalyzer.corrJetTag = cms.InputTag('corrJetDistinctNonIsoTauSelector')
process.highMTMuHadNonIsoTauAnalyzer.reweight = cms.bool(False)
process.lowMTMuHadNonIsoTauAnalyzer = process.highMTMuHadNonIsoTauAnalyzer.clone()
process.lowMTMuHadNonIsoTauAnalyzer.outFileName = cms.string('file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadNonIsoAnalysis_lowMT_DYJetsToLL_M-50_v2.root')

#analyze all taus
process.highMTMuHadTauAnalyzer = process.highMTMuHadIsoTauAnalyzer.clone()
process.highMTMuHadTauAnalyzer.outFileName = cms.string(
    'file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadAnalysis_highMT_DYJetsToLL_M-50_v2.root'
    )
process.highMTMuHadTauAnalyzer.tauTag = cms.InputTag('AllBVetoFilter', '', 'MUHADANALYSIS')
process.highMTMuHadTauAnalyzer.corrJetTag = cms.InputTag('corrJetDistinctTauSelector')
process.lowMTMuHadTauAnalyzer = process.highMTMuHadTauAnalyzer.clone()
process.lowMTMuHadTauAnalyzer.outFileName = cms.string('file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadAnalysis_lowMT_DYJetsToLL_M-50_v2.root')

#output
process.output = cms.OutputModule(
    "PoolOutputModule",
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
    fileName = cms.untracked.string(
    'file:/mnt/hadoop/store/user/kmtos/data1/kmtos/DYJetsToLL/EDM_files/DYJetsToLL_M-50_v2.root'
    )
    )

#MET filter
process.METFilter.minMET = cms.double(30.)
process.METFilter.METTag = cms.InputTag("patType1CorrectedPFMetPFlow")

#MT filter
process.MTFilter.minMT = cms.double(50.)
process.MTFilter.METTag = cms.InputTag("patType1CorrectedPFMetPFlow")
process.highMTFilter = process.MTFilter.clone()
process.lowMTFilter = process.MTFilter.clone()
process.lowMTFilter.passFilter = cms.bool(False)

#OS filter for tau_mu W_mu charge product
process.OSSFFilterIso = cms.EDFilter('OSSFFilter',
                                  WMuonTag = cms.InputTag('WIsoMuonSelector'),
                                  tauTag = cms.InputTag('IsoBVetoFilter'),
                                  jetMuonMapTag = cms.InputTag('CleanJets', '', 'SKIM'),
                                     passFilter = cms.bool(True)
                                  )
process.OSSFFilterNonIso = process.OSSFFilterIso.clone()
process.OSSFFilterNonIso.tauTag = cms.InputTag('NonIsoBVetoFilter')
process.OSSFFilter = process.OSSFFilterIso.clone()
process.OSSFFilter.tauTag = cms.InputTag('AllBVetoFilter', '', 'MUHADANALYSIS')

#SS filter for tau_mu tau_had charge product
process.SSSFFilterIso = cms.EDFilter('SSSFFilter',
##                                   WMuonTag = cms.InputTag('WIsoMuonSelector'),
                                  tauTag = cms.InputTag('IsoBVetoFilter'),
                                  jetMuonMapTag = cms.InputTag('CleanJets', '', 'SKIM'),
                                     passFilter = cms.bool(True)
                                  )
process.SSSFFilterNonIso = process.SSSFFilterIso.clone()
process.SSSFFilterNonIso.tauTag = cms.InputTag('NonIsoBVetoFilter')
## process.SSSFFilterNonIso.passFilter = cms.bool(False)
process.SSSFFilter = process.SSSFFilterIso.clone()
process.SSSFFilter.tauTag = cms.InputTag('AllBVetoFilter', '', 'MUHADANALYSIS')

#muon trigger object filter
process.muonTriggerObjectFilter = cms.EDFilter(
    'MuonTriggerObjectFilter',
    recoObjTag = cms.InputTag("WIsoMuonSelector"),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    triggerDelRMatch = cms.untracked.double(0.1),
    hltTags = cms.VInputTag(cms.InputTag("HLT_IsoMu24_eta2p1_v1", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v2", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v3", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v4", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v5", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v6", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v7", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v8", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v9", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v10", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v11", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v12", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v13", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v14", "", "HLT"),
                            cms.InputTag("HLT_IsoMu24_eta2p1_v15", "", "HLT")
                            ),
    theRightHLTTag = cms.InputTag("HLT_IsoMu24_eta2p1"),
    theRightHLTSubFilter = cms.InputTag("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3cr"),
    HLTSubFilters = cms.untracked.VInputTag("")
    )

#sequences
process.beginSequence = cms.Sequence(
    process.genWMuNuSelector*
    process.genWTauNuSelector*
    process.genPartonSelector*
    process.genMuSelector*
    process.genTauMuSelector
    )
process.baseIsoTauAnalysisSequence = cms.Sequence(
    process.muHadIsoTauSelector*
    process.IsoBVetoFilter*
    process.corrJetDistinctIsoTauSelector*
    process.muonTriggerObjectFilter*
    process.OSSFFilterIso*
    process.SSSFFilterIso
    )
process.highMTIsoTauAnalysisSequence = cms.Sequence(
    process.baseIsoTauAnalysisSequence*
    process.highMTFilter*
    process.highMTMuHadIsoTauAnalyzer
    )
process.lowMTIsoTauAnalysisSequence = cms.Sequence(
    process.baseIsoTauAnalysisSequence*
    process.lowMTFilter*
    process.lowMTMuHadIsoTauAnalyzer
    )
process.baseSignalIsoTauAnalysisSequence = cms.Sequence(
    process.genWMuNuSelector*
    process.IsoMu24eta2p1Selector*
    process.WMuonPTSelector*
    process.WIsoMuonSelector*
    process.tauMuonPTSelector*
    process.tauMuonSelector*
    process.PFTau*
    process.muHadIsoTauSelector*
    process.IsoBVetoFilter*
    process.muonTriggerObjectFilter*
    process.OSSFFilterIso*
    process.SSSFFilterIso
    )
process.highMTSignalIsoTauAnalysisSequence = cms.Sequence(
    process.baseSignalIsoTauAnalysisSequence*
    process.highMTFilter*
    process.highMTMuHadIsoTauAnalyzer
    )
process.lowMTSignalIsoTauAnalysisSequence = cms.Sequence(
    process.baseSignalIsoTauAnalysisSequence*
    process.lowMTFilter*
    process.lowMTMuHadIsoTauAnalyzer
    )
process.baseNonIsoTauAnalysisSequence = cms.Sequence(
    process.muHadNonIsoTauSelector*
    process.NonIsoBVetoFilter*
    process.corrJetDistinctNonIsoTauSelector*
    process.muonTriggerObjectFilter*
    process.OSSFFilterNonIso*
    process.SSSFFilterNonIso
    )
process.highMTNonIsoTauAnalysisSequence = cms.Sequence(
    process.baseNonIsoTauAnalysisSequence*
    process.highMTFilter*
    process.highMTMuHadNonIsoTauAnalyzer
    )
process.lowMTNonIsoTauAnalysisSequence = cms.Sequence(
    process.baseNonIsoTauAnalysisSequence*
    process.lowMTFilter*
    process.lowMTMuHadNonIsoTauAnalyzer
    )
process.baseTauAnalysisSequence = cms.Sequence(
    process.muHadTauSelector*
    process.AllBVetoFilter*
    process.corrJetDistinctTauSelector*
    process.muonTriggerObjectFilter*
    process.OSSFFilter*
    process.SSSFFilter
    )
process.highMTTauAnalysisSequence = cms.Sequence(
    process.baseTauAnalysisSequence*
    process.highMTFilter*
    process.highMTMuHadTauAnalyzer
    )
process.lowMTTauAnalysisSequence = cms.Sequence(
    process.baseTauAnalysisSequence*
    process.lowMTFilter*
    process.lowMTMuHadTauAnalyzer
    )

#path
process.begin = cms.Path(process.beginSequence)
process.highMT = cms.Path(process.highMTNonIsoTauAnalysisSequence)
process.lowMT = cms.Path(process.lowMTNonIsoTauAnalysisSequence)
process.schedule = cms.Schedule(process.begin,process.highMT,process.lowMT)
## process.e = cms.EndPath(process.output)
