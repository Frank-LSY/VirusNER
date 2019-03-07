#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:46:08 2019

@author: frank-lsy
"""

import pandas as pd

for i in range(300):
    tmp = pd.read_csv('../labeled-token/{}.tsv'.format(i+1),sep='\t',header=0)
    bieo = tmp['BIEO']
    for j in range(len(bieo)):
        if (bieo[j]=='B' or bieo[j]=='B-virs'):
            print(i)