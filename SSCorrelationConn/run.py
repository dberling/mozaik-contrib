# -*- coding: utf-8 -*-
"""
"""
import sys
from pyNN import nest
import mozaik.controller
from mozaik.controller import run_workflow, setup_logging
import mozaik
from experiments import create_experiments
from model import SSCorrelationConnectivity
from mozaik.storage.datastore import Hdf5DataStore,PickledDataStore
from analysis_and_visualization import perform_analysis_and_visualization
from parameters import ParameterSet

try:
    from mpi4py import MPI
except ImportError:
    MPI = None
if MPI:
    mpi_comm = MPI.COMM_WORLD
MPI_ROOT = 0

if True:
    data_store,model = run_workflow('SSCorrelationConnectivity',SSCorrelationConnectivity,create_experiments)
else: 
    setup_logging()
    data_store = PickledDataStore(load=True,parameters=ParameterSet({'root_directory':'SSCorrelationConnectivity_A_____', 'store_stimuli' : False}),replace=True)

if mpi_comm.rank == 0:
   print "Starting visualization" 
   perform_analysis_and_visualization(data_store)
   data_store.save() 
