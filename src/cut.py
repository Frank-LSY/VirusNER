#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:19:18 2019
自由软件能卖钱吗？
@author: frank-lsy
"""

import os
import time
import sh
import re

#viruses = os.listdir("../abstracts")
#print(viruses)
viruses = ["human-neck-virus"]
for virus in viruses:
    file = "../abstracts/{}/pubmed_result.txt".format(virus)
    abstract = ''
    i = 1
    for raw_line in open(file):
        abstract += raw_line
        eoa_flag = re.search("Indexed for MEDLINE]",raw_line)
        #print(type(eoa_flag))
        if (eoa_flag != None):
            print(abstract)
            #time.sleep(3)
            f = open("../abstracts/{}/{}.txt".format(virus,i),'w')
            f.write(abstract)
            i += 1
            abstract = ''
            f.close()
        #print(raw_line)
    #time.sleep(5)