// -*- C++ -*-
//
// modified from V0Fitter. It is a cmssw code used in RECO and AOD. To find mumutktk combinations.
// It is fitting method 1 for vertexing.
// This candidate is composed by mu + mu + tk + tk. with a constrain mumu with J/psi mass.
// If constrain mass is smaller than 0. the constrain is disabled.
//
// ############################## NOTICE #########################################################
// The preselection is tktk - mumu vertex position need to SMALLER than n_1 sigma.
// ############################## NOTICE #########################################################
//
//
//
// modified from V0Fitter. It is a cmssw code used in RECO and AOD. To find Lambda0 and Kshort
// Package:    V0Producer
// Class:      V0Fitter
//
/**\class V0Fitter V0Fitter.h RecoVertex/V0Producer/interface/V0Fitter.h

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Brian Drell
//         Created:  Fri May 18 22:57:40 CEST 2007
// $Id: V0Fitter.h,v 1.22 2010/06/19 03:24:33 drell Exp $
//
//

#ifndef __fourTracksFittingMethod1_H__
#define __fourTracksFittingMethod1_H__

#include "vertexProducer/vertexProducer/interface/fourTracksFitter.h"

class fourTracksFittingMethod1 : public fourTracksFitter
{
public:
    fourTracksFittingMethod1(const edm::ParameterSet& theParams,
                edm::ConsumesCollector&& iC ): fourTracksFitter(theParams, std::move(iC)) {}
    virtual ~fourTracksFittingMethod1() {};
    virtual void fitAll(const edm::Event& iEvent, const edm::EventSetup& iSetup);

};

#endif
