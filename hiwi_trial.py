#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 12:13:03 2022

@author: ashin
"""

import pandas as pd
import os
import glob
# from numpy import genfromtxt

# use glob to get all the csv files
# in the folder

## Change the path as needed for IMu or mocap data with respective subject folder

path = os.getcwd()+"/Data/IMU data/S07" ##### change here (only) to work with different subjects and sensor.

print(path)
csv_files = glob.glob(os.path.join(path, "*.csv"))



 # looping over the list of csv files in a particular subject folder
     
for f in csv_files:
    df=pd.read_csv(f,sep=',',header=None).values
    ##Converting csv to numpy array
    # df=pd.read_csv(f)
    print('Location: ',f)
    print("File Name:",f.split("/")[-1])
    x=f.split("/")[-1]
    
    print("Content:")
    # my_array=genfromtxt(x,delimiter=',')
    # display(df) or (display used to see the data type with results)
    print(df)
   
     
