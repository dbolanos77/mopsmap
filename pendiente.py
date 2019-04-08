# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:10:13 2019

@author: Daniela Bolaños
"This program read the input mopsmap file, run mopsmap and save as array the results of the simulation"""
import numpy as np
import subprocess

#read input file
path_mopsmap_executable='/home/user/Documentos/MOPSMAP/mopsmap/mopsmap'
path_optical_dataset='/home/user/Documentos/MOPSMAP/main_data_base/optical_dataset/'
path_input = '/home/user/Documentos/MOPSMAP/mopsmap/input/input_mopsmap.txt'

#write optical_dataset over the input file
mopsmap_input_file = open(path_input,'a')
mopsmap_input_file.write('scatlib \'%s\'\n'%path_optical_dataset)
mopsmap_input_file.write('output ascii_file input_mopsmap.txt')
#read rH from input file
line = open(path_input, "r").readlines()[5]
rH = float(line.strip('rH'))
mopsmap_input_file.close()

RH = []
  # start mopsmap
p = subprocess.Popen([path_mopsmap_executable, path_input], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
stdout1,stderr1 = p.communicate()

if stdout1 or stderr1:
  if stdout1:
   print stdout1
  if stderr1:
   print stderr1
   raise SystemExit()
   
# read the mopsmap output files into numpy arrays
output_integrated=np.loadtxt('input_mopsmap.txt.integrated',ndmin=1,dtype=[('wvl', 'f8'),('ext_coeff', 'f8'), ('ssa','f8'),('g','f8'),('r_eff','f8'),('n','f8'),('a','f8'),('v','f8'),('m','f8'),('ext_angstrom','f8'),('sca_angstrom','f8'),('abs_angstrom','f8')])
output_matrix=np.loadtxt('input_mopsmap.txt.scattering_matrix',ndmin=1,dtype=[('wvl', 'f8'),('angle', 'f8'), ('a1','f8'),('a2','f8'),('a3','f8'),('a4','f8'),('b1','f8'),('b2','f8')])
output_vol_scat=np.loadtxt('input_mopsmap.txt.volume_scattering_function',ndmin=1,dtype=[('wvl', 'f8'),('angle', 'f8'), ('a1_vol','f8')])
output_lidar=np.loadtxt('input_mopsmap.txt.lidar',ndmin=1,dtype=[('wvl', 'f8'),('ext_coeff', 'f8'), ('back_coeff','f8'), ('S','f8'), ('delta_l','f8'),('ext_angstrom','f8'),('back_angstrom','f8')])
output_phase_function=np.loadtxt('input_mopsmap.txt.phase_function')


