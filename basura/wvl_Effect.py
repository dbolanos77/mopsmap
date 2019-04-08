import mopsmap_interface
import numpy as np

# different types of wavelength input
wvl=(0.355,0.532,1.064)
#wvl=0.532
#wvl=np.linspace(0.4,1.0,num=7) 

# size equivalence
#size_equ='vol'
size_equ='cs'

# two log-normal modes
#n=(1.*10**8,0.5*10**8) # concentration in m-3
n=1.*10**8
#r_mod=(0.1,0.4)
#sigma=(2.6,2.2)
#r_min=0.01
#r_max=10

r_mod=(0.209)
sigma=(2.03)
r_min=0.005
r_max=20

# refractive index
#m="1.54 0.002"
#m=("1.54 0.000","1.56 0.01")
m="1.53 0.008"
#nonabs_fraction=0.5
nonabs_fraction=0.

#shape="spheroid oblate 1.7"
shape="spheroid prolate 1.5"

num_theta=2

results=mopsmap_interface.call_mopsmap(wvl,size_equ,n,r_mod,sigma,r_min,r_max,m,nonabs_fraction,shape,num_theta)

for i_wvl in range(len(results['wvl'])):
  if i_wvl>0:
    print 
    print '  extinction angstrom:      %8.4f'%results['ext_angstrom'][i_wvl]
    print '  scattering angstrom:      %8.4f'%results['sca_angstrom'][i_wvl]
    print '  absorption angstrom:      %8.4f'%results['abs_angstrom'][i_wvl]
    print '  backscatter angstrom:     %8.4f'%results['back_angstrom'][i_wvl]
  print 
  print '  extinction coeff.:          %8.4e m^-1'%(results['ext_coeff'][i_wvl])
  print '  asymetry parameter.:        %8.4e m^-1'%(results['g'][i_wvl])
  print '  single scattering albedo:   %8.4f'%(results['ssa'][i_wvl])
  print '  backscatter coef.:          %8.4e m^-1 sr^-1'%results['back_coeff'][i_wvl]
  print '  lidar ratio:                %8.4f sr'%results['S'][i_wvl]
  print '  lin. depol. ratio           %8.4f'%results['delta_l'][i_wvl] 







