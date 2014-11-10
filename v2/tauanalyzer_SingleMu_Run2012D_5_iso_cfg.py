import FWCore.ParameterSet.Config as cms

process = cms.Process("MUHADANALYSIS")

#PDG IDs
A_PDGID = 36
Z_PDGID = 23
W_PDGID = 24
TAU_PDGID = 15
MU_PDGID = 13
NUMU_PDGID = 14
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

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

readFiles = cms.untracked.vstring()
process.source = cms.Source(
    "PoolSource",
    fileNames = readFiles,
    skipEvents = cms.untracked.uint32(0)
    )
readFiles.extend([
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_501_3_mSo.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_502_1_6zg.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_503_1_Br6.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_504_1_Zqq.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_505_1_as2.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_506_1_9u3.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_507_1_dce.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_508_2_fNq.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_509_2_9EL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_50_1_EYc.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_510_2_Dyc.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_511_1_aXW.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_512_3_igV.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_513_1_cX5.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_514_1_4Ov.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_515_1_3AJ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_516_1_bcK.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_517_1_e7f.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_518_1_5z2.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_519_1_VZW.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_51_1_E9W.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_520_1_V7A.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_521_1_g04.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_522_1_Ofy.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_523_1_sEF.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_524_1_O12.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_525_2_lBg.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_526_2_amH.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_527_1_iX8.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_528_1_rib.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_529_1_ksu.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_52_1_1D5.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_530_1_m98.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_531_1_bfh.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_532_1_Ts4.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_533_1_v5G.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_534_1_156.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_535_1_FzW.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_536_1_RaH.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_537_1_eLp.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_538_1_OtT.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_539_1_zfB.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_53_1_CZE.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_540_1_KSP.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_541_2_jlZ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_542_3_2a7.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_543_1_A72.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_544_2_pog.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_545_2_jqI.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_546_1_Yek.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_547_1_kyZ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_548_1_dlh.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_549_1_fIe.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_54_1_MFk.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_550_1_hHV.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_551_1_pVJ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_552_2_48g.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_553_2_utu.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_554_1_TsL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_555_2_89o.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_556_1_0f5.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_557_1_6Oa.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_558_1_ICH.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_559_1_pf8.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_55_1_PY3.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_560_1_o7y.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_561_1_PKd.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_562_1_2u8.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_563_1_4hL.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_564_1_EO8.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_565_1_7tv.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_566_1_U7y.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_567_1_wqE.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_568_1_G7V.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_569_1_hnM.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_56_1_3gf.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_570_1_KMI.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_571_1_YaQ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_572_1_S1O.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_573_2_5uD.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_574_1_xUr.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_575_1_1mr.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_576_1_A6I.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_577_1_XzS.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_578_1_nus.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_579_1_cuo.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_57_1_6TW.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_580_1_1SJ.root',
    'file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/SingleMu_Run2012D-22Jan2013-v1_AOD_skim_v3/data_no_selection_581_1_7ze.root',
    ])

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck') #speed?

#for L1GtStableParametersRcd and jet corrections
#START52_V9B is recommended for JEC in Summer12 CMSSWv5.2 MC
#START52_V9 is what the Summer12 CMSSWv5.2 MC was produced with
#START53_V15 is the latest recommended JEC tag
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('FT_53_V21_AN4::All')

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
    minNumGenObjectsToPassFilter = cms.uint32(1),
    makeAllCollections = cms.bool(False)
    )

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

#clean the jets of soft muons, then rebuild the taus
process.CleanJets.muonSrc = cms.InputTag('tauMuonSelector')
process.CleanJets.PFCandSrc = cms.InputTag('particleFlow')
process.CleanJets.cutOnGenMatches = cms.bool(False)
process.CleanJets.outFileName = cms.string(
    'file://home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/NMSSMSignal_MuProperties_SingleMu_Run2012D_5.root'
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
process.pfJetMETcorr.jetCorrLabel = cms.string("ak5PFL1FastL2L3Residual")

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
    'file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadIsoAnalysis_highMT_SingleMu_Run2012D_5_v2.root'
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
    genParticleTag = cms.InputTag('genPartonSelector'),
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
    MC = cms.bool(False),
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
process.lowMTMuHadIsoTauAnalyzer.outFileName = cms.string('file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadIsoAnalysis_lowMT_SingleMu_Run2012D_5_v2.root')

#analyze non-isolated taus
process.highMTMuHadNonIsoTauAnalyzer = process.highMTMuHadIsoTauAnalyzer.clone()
process.highMTMuHadNonIsoTauAnalyzer.outFileName = cms.string(
    'file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadNonIsoAnalysis_highMT_SingleMu_Run2012D_5_v2.root'
    )
process.highMTMuHadNonIsoTauAnalyzer.tauTag = cms.InputTag('NonIsoBVetoFilter')
process.highMTMuHadNonIsoTauAnalyzer.corrJetTag = cms.InputTag('corrJetDistinctNonIsoTauSelector')
process.lowMTMuHadNonIsoTauAnalyzer = process.highMTMuHadNonIsoTauAnalyzer.clone()
process.lowMTMuHadNonIsoTauAnalyzer.outFileName = cms.string('file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadNonIsoAnalysis_lowMT_SingleMu_Run2012D_5_v2.root')

#analyze all taus
process.highMTMuHadTauAnalyzer = process.highMTMuHadIsoTauAnalyzer.clone()
process.highMTMuHadTauAnalyzer.outFileName = cms.string(
    'file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadAnalysis_highMT_SingleMu_Run2012D_5_v2.root'
    )
process.highMTMuHadTauAnalyzer.tauTag = cms.InputTag('AllBVetoFilter', '', 'MUHADANALYSIS')
process.highMTMuHadTauAnalyzer.corrJetTag = cms.InputTag('corrJetDistinctTauSelector')
process.lowMTMuHadTauAnalyzer = process.highMTMuHadTauAnalyzer.clone()
process.lowMTMuHadTauAnalyzer.outFileName = cms.string('file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadAnalysis_lowMT_SingleMu_Run2012D_5_v2.root')

#output
process.output = cms.OutputModule(
    "PoolOutputModule",
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
    fileName = cms.untracked.string(
    'file:/mnt/hadoop/store/user/kmtos/data1/kmtos/data/EDM_files/SingleMu_Run2012D_5_v2.root'
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

#photon trigger object filter
process.photonTriggerObjectFilter = cms.EDFilter(
    'PhotonTriggerObjectFilter',
    recoObjTag = cms.InputTag("photonSelector"),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    triggerDelRMatch = cms.untracked.double(0.1),
    hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1", "",
                 "HLT")
    ),
    theRightHLTTag = cms.InputTag(
    "HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned"
    ),
    theRightHLTSubFilter = cms.InputTag(
    "hltPhoton30R9Id90CaloIdHE10Iso40EBOnlyTrackIsoLastFilter"
    ),
    HLTSubFilters = cms.untracked.VInputTag("")
    )

#sequences
process.beginSequence = cms.Sequence(process.genPartonSelector*process.genMuSelector)
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
process.highMT = cms.Path(process.highMTIsoTauAnalysisSequence)
process.lowMT = cms.Path(process.lowMTIsoTauAnalysisSequence)
process.schedule = cms.Schedule(process.highMT,process.lowMT)
## process.e = cms.EndPath(process.output)


