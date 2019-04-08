# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:18:24 2019
Este programa ejecuta mopsmap con los inputs que se generan a partir del programa tmp_inputs_bash.sh
@author: Daniela Bolaños
"""
import os
import glob
import numpy as np
import shutil
import subprocess
import matplotlib.pyplot as plt

path_mopsmap_executable='/home/user/Documentos/MOPSMAP/mopsmap/mopsmap'
path_optical_dataset='/home/user/Documentos/MOPSMAP/main_data_base/optical_dataset/'
input_folder='/home/user/Documentos/MOPSMAP/mopsmap/input'
output_folder='./outputdir1'
#write in each file the optical path and the ascii file format name 
RH=[]
out_integrated = []
ext_coeff = []
out_lidar= []
delta = []

#out_integrated = np.empty((3, 12)) #filas, columnas
for root, dirs, files in os.walk("/home/user/Documentos/MOPSMAP/mopsmap/input"):  
    for filename in files:   
        path_input=os.path.join(input_folder,filename)
        #print(path_input)
        mopsmap_input_file = open(path_input,'a')
        mopsmap_input_file.write('scatlib \'%s\'\n'%path_optical_dataset)
        mopsmap_input_file.write('output ascii_file \'%s\'\n'%filename)
#read rH for each file
        line = open(path_input, "r").readlines()[5]
        rH = float(line.strip('rH'))
        RH.append(rH)
#close openned file
        mopsmap_input_file.close()
# start mopsmap
        p = subprocess.Popen([path_mopsmap_executable, path_input], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        stdout1,stderr1 = p.communicate()
        if stdout1 or stderr1:
         if stdout1:
          print stdout1
         if stderr1:
          print stderr1
          raise SystemExit()
#outputs
        output_integrated=np.loadtxt(filename+".integrated")    
        out_integrated.append(output_integrated.T)
        output_matrix=np.loadtxt(filename+".scattering_matrix")
        output_vol_scat=np.loadtxt(filename+".volume_scattering_function")
        output_lidar=np.loadtxt(filename+".lidar")
        out_lidar.append(output_lidar.T)
        output_phase_function=np.loadtxt(filename+".phase_function")
#extinction coefficient in m −1
        for lista in out_integrated:
         e=lista[1]
        ext_coeff.append(e)
#linear depolarization
        for lista in out_lidar:
         e=lista[4]
        delta.append(e)     
   
RH = np.hstack(RH)
delta = np.hstack(delta)

#plot RH vs delta particulas: https://matplotlib.org/tutorials/introductory/pyplot.html
plt.plot(RH, delta, 'ro',label='sea salt properties\n k=0.5\n del_point=50%')
plt.ylabel('$\delta$ particles')
plt.xlabel('Relative Humidity %')
plt.legend(loc='lower left',fontsize=12)
plt.show()

#Mover outputs a otra carpeta
#for file in glob.glob("/home/user/Documentos/MOPSMAP/mopsmap/code/*.txt.*"):  
#    shutil.move(file, "./outputdir1")   
         