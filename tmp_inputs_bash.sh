#!/bin/bash

#for runnig typ in terminal: this_program_path bash tmp_inputs_bash.sh 
#this program create inputs with a rang of rh and a rang of aspect ratio.

#### PARAMETERS###
mopsmap_path="/home/user/Documentos/MOPSMAP/mopsmap"
optical_dataset="/home/user/Documentos/MOPSMAP/main_data_base/optical_dataset"
idir="$mopsmap_path/input"
#TEMPLATE="$idir/tmp.txt"
TEMPLATE="$mopsmap_path/tmp_salt.txt"
rhlist=(0 10 20 30 40 50 60 70 80 90)
sizelist=(1.2 1.2 1.2 1.2 1.2 1.2 1.12592593 1.05185185 1 1) #pegar aqui el resultado de programa RH_vs_aspectRatio.py

#sizelist=(1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1 1) 


#### EXECUTION ####
current_dir=`pwd`
echo "INFO: RH list is ${rhlist[@]}"
echo "INFO: size list is ${sizelist[@]}"
n=0
while [ $n -lt ${#rhlist[*]} ]; do
  tmprh=${rhlist[$n]}
  tmpsize=${sizelist[$n]}	
  echo "Step $n: $tmprh $tmpsize"  
  nsize=$(echo "$tmpsize" | sed "s/\.//g")
  echo "Name string nsize: $nsize"
  tmp="$idir/input_mopsmap_${tmprh}_${nsize}.txt"
  cp $TEMPLATE $tmp
 # echo "INFO: Creating input file for : $tmp"
  sed -i "s/<rh_param>/$tmprh/g" $tmp
  sed -i "s/<size_param>/$tmpsize/g" $tmp
  n=$(($n+1)) 
done

