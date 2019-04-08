# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:53:42 2019

@author: user
"""

import numpy as np
import subprocess
import glob
import shutil
import matplotlib.pyplot as plt

path_mopsmap_executable='/home/user/Documentos/MOPSMAP/mopsmap/mopsmap'
path_optical_dataset='/home/user/Documentos/MOPSMAP/main_data_base/optical_dataset/'
path_input = '/home/user/Documentos/MOPSMAP/mopsmap/RESULTS/refIndex_delta/inp'
output_folder='/home/user/Documentos/MOPSMAP/mopsmap/RESULTS/refIndex_delta/output'

#parameters
#log_normal size distribution parameters 
n=1.*10**8 # concentration in m-3
r_mod=0.1
sigma=2.6
r_min=0.01
r_max=10
#refractive index opac
#m_real = [1.53, 1.33, 1.53, 1.5, 1.431, 1.53]
#m_im = [0.008, 3.7e-09, 0.0055, 1.55e-08, 1e-08, 0.005]

#m_im = [0.008, 3.7e-09, 0.0055, 1.55e-08, 1e-08, 0.005, 0.1, 0.12, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0]
#m_real = [1.53] * len(m_im),

m_real = [1.28, 1.29, 1.3, 1.31, 1.32, 1.33, 1.34, 1.35, 1.36, 1.37, 1.38, 1.39, 1.4, 1.41, 1.42, 1.43, 1.44, 1.45, 1.46, 1.47, 1.48, 1.49, 1.5, 1.51, 1.52, 1.53, 1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.6, 1.61, 1.62]
m_im = [0.00]*len(m_real)
shape = 'spheroid prolate 1.5'
#nonabs_fraction =0 #non absorbiing fraction
kappa = 0.5
density = 2
rH = 0
size_equ='cs'
num_theta=4
wvl = 0.532

deltas = []
im =  []

for i in range (len(m_real)):
#write mopsmap input file
    mopsmap_input_file = open(path_input,'w')
    mopsmap_input_file.write('size log_normal %s %s %s %s %s\n'%(r_mod,sigma,n,r_min,r_max))
    mopsmap_input_file.write('refrac  %s %s\n'%(m_real[i], m_im[i]))
    mopsmap_input_file.write('shape %s\n'%shape)
    #mopsmap_input_file.write('refrac nonabs_fraction %s\n'%nonabs_fraction)    
    mopsmap_input_file.write('kappa %s\n'%kappa)  
    mopsmap_input_file.write('density %s\n'%density)
    mopsmap_input_file.write('rH %s\n'%rH)
    mopsmap_input_file.write('size_equ %s\n'%size_equ)
    #mopsmap_input_file.write('output num_theta %i\n'%num_theta)
    mopsmap_input_file.write('wavelength %s\n'%wvl)
    mopsmap_input_file.write('output integrated\n')
    mopsmap_input_file.write('output scattering_matrix\n')
    mopsmap_input_file.write('output volume_scattering_function\n')
    mopsmap_input_file.write('output phase_function\n')
    mopsmap_input_file.write('output lidar\n')
   #mopsmap_input_file.write('output digits 15\n')        
    mopsmap_input_file.write('scatlib \'%s\'\n'%path_optical_dataset)
    mopsmap_input_file.write('output ascii_file out')
    mopsmap_input_file.close()
#start mopsmap
    p = subprocess.Popen([path_mopsmap_executable, path_input], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    stdout1,stderr1 = p.communicate()
    if stdout1 or stderr1:
     if stdout1:
      print stdout1
     if stderr1:
      print stderr1
     raise SystemExit()
#read the mopsmap output files into numpy arrays
    output_integrated=np.loadtxt('out.integrated',ndmin=1,dtype=[('wvl', 'f8'),('ext_coeff', 'f8'), ('ssa','f8'),('g','f8'),('r_eff','f8'),('n','f8'),('a','f8'),('v','f8'),('m','f8'),('ext_angstrom','f8'),('sca_angstrom','f8'),('abs_angstrom','f8')])
    output_matrix=np.loadtxt('out.scattering_matrix',ndmin=1,dtype=[('wvl', 'f8'),('angle', 'f8'), ('a1','f8'),('a2','f8'),('a3','f8'),('a4','f8'),('b1','f8'),('b2','f8')])
    output_vol_scat=np.loadtxt('out.volume_scattering_function',ndmin=1,dtype=[('wvl', 'f8'),('angle', 'f8'), ('a1_vol','f8')])
    output_lidar=np.loadtxt('out.lidar',ndmin=1,dtype=[('wvl', 'f8'),('ext_coeff', 'f8'), ('back_coeff','f8'), ('S','f8'), ('delta_l','f8'),('ext_angstrom','f8'),('back_angstrom','f8')])
    output_phase_function=np.loadtxt('out.phase_function')
#delta
    delta = output_lidar['delta_l']
    deltas.append(delta)
    im.append(m_im)
    
#plot imaginary part of ref_index vs delta
#plt.plot(m_im,deltas, 'b*', label='m_real = 1.53')
#plt.title('Influence of imaginary part of refractive index',fontsize=14)
#plt.ylabel('$\delta$ particles', fontsize=12) 
#plt.xlabel('Imaginary part of refractive index %',fontsize=12)
#plt.legend(loc='upper right',fontsize=12)
#plt.show()

#plot real part of ref_index vs delta
plt.plot(m_real,deltas, 'b-*', label='m_im = 0')
plt.title('Influence of real part of refractive index',fontsize=14)
plt.ylabel('$\delta$ particles', fontsize=12) 
plt.xlabel(' real part of refractive index %',fontsize=12)
plt.legend(loc='upper right',fontsize=12)
plt.show()


#Mover outputs a otra carpeta
#for file in glob.glob("/home/user/Documentos/MOPSMAP/mopsmap/code/out.*"):  
   # shutil.move(file, "./outputdir1")  
  #  shutil.move(file, output_folder) 







