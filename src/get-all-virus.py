#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:02:27 2019

@author: frank-lsy
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('./raw-html.html'))
#print(soup.prettify())
f = open('../table/all-virus.txt','w')
i = 0
for link in soup.find_all('ul'):
    if (i<2):
        i +=1
        continue
    i += 1
    for li in link.find_all('a'):
        f.write(li.string+'\n')
        print(li.string)
f.close()
#print(soup.select('.div-col columns column-width')[0].text)