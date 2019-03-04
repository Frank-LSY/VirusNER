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
import xml.dom.minidom

dom = xml.dom.minidom.parse('../raw/human-neck-virus.xml')
root = dom.documentElement
bb = root.getElementsByTagName('AbstractText')
#print(bb[0].firstChild.data)
for i in range(3188):
    #print(b.firstChild.data)
    f = open("../abstracts/human-neck-virus/{}.txt".format(i+1),"w")
    f.write(bb[i].firstChild.data)
    f.close()
#print (type(b.firstChild.data))
"""
#viruses =os.listdir("../abstracts")
viruses = ['human-neck-virus']
for virus in viruses:
    file = "../raw/{}.txt".format(virus)
    abstract = ''
    i = 1
    for raw_line in open(file):
        #raw_line = raw_line.strip("\n")
        print(raw_line)
        abstract += raw_line
        eoa_flag = re.search("Indexed for MEDLINE]",raw_line)
        #print(type(eoa_flag))
        if (eoa_flag != None):
            #print(abstract)
            #time.sleep(3)
            f = open("../abstracts/{}/{}.txt".format(virus,i),'w')
            f.write(abstract)
            i += 1
            abstract = ''
            f.close()
        #print(raw_line)
    #time.sleep(5)
"""

