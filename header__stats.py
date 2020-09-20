#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:37:13 2018

@author: amanohar
"""
import sys
#sys.path.append('/home/psr')
import subprocess
import glob
import os
import csv
import sigpyproc
from sigpyproc.Readers import FilReader
#from struct import unpack
#joblib module

w=open('Headerparams_11.txt','w')
#k=open('header_08.txt','w')
#directory = "/beegfsBN/miraculix/part3/aswin/filfiles"
sigproc_path = "/home/psr/software/psrsoft/usr/bin/"
data = glob.glob("/home/psr/PTTAPES1/PT_TAPES_archive11_1/PT0*/PT*")

#Create fil files from raw data#
###################################################
for i in range(len(data)):
    cmds = sigproc_path + 'filterbank ' + data[i] + ' ' + '-o ' + '/home/psr/PTTAPES1/PT_TAPES_archive11_1/' + os.path.basename(data[i]) + '_8.fil' 
    subprocess.check_output(cmds, shell=True)
#filterbank_data = glob.glob('/home/psr/PTTAPES1/aswin_data/PT0159_101_8.fil')

with open('out.txt','w') as f:
def process_filterbank(filename):
filterbank_data = glob.glob('/home/psr/PTTAPES1/aswin_data_11/*.fil')
print filterbank_data
for i in range(len(filterbank_data)):
    print filterbank_data[i]
    fil_data= FilReader(filterbank_data[i])
    number_samples= fil_data.header.nsamples
    obs_time_seconds= fil_data.header.tobs
    sampling_time= fil_data.header.tsamp
    channels= fil_data.header.nchans
    source= fil_data.header.source_name
    central= fil_data.header.fcenter
    band= fil_data.header.bandwidth
    name= fil_data.header.filename
    observation_time= fil_data.header.tobs

    #print number_samples,source,channels
    #print name
    #print >> f, sampling_time
    #print >> a, central
    #print >> b, channels
    #print >> c, band
    #print >> d, name
    #print >> e, source
    print >> w, source,channels,band,central,sampling_time,observation_time,name 
    #print >> f, 'Time:', sampling_time
    #print >> f, 'Chan:', channels
    
#if name__===main:
    #start_range = sys.argv[1]
    #end_range = sys.argv[2]
    #num_cores = 24
  
    #joblib(num_cores)(process_filterbank)(file) for i in range(start_range, end_range) 

   


