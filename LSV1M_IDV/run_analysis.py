# -*- coding: utf-8 -*-
"""
"""
import matplotlib
matplotlib.use('Agg')

import sys
from mozaik.controller import setup_logging
import mozaik
from mozaik.storage.datastore import Hdf5DataStore,PickledDataStore
from analysis_and_visualization import perform_analysis_and_visualization,perform_analysis_and_visualization_conn,perform_analysis_and_visualization_or,perform_analysis_and_visualization_stc,perform_analysis_and_visualization_octc,perform_analysis_and_visualization_spont,perform_analysis_and_visualization_or_small
from parameters import ParameterSet

from mozaik.controller import Global
Global.root_directory = sys.argv[1]+'/'

setup_logging()
data_store = PickledDataStore(load=True,parameters=ParameterSet({'root_directory':sys.argv[1],'store_stimuli' : False}),replace=True)

perform_analysis_and_visualization_or_small(data_store)
data_store.save() 
