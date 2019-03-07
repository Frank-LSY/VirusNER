#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 08:05:23 2019

@author: frank-lsy
"""

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
a = open("../count.txt",'w')
j = 1
for i in range(1,303):
    a.write(str(i)+'.')
    f = open("../abstracts/human-neck-virus/{}.txt".format(i),'r')
    abstract = f.read()
    abstract.replace("\n","")
    sents = sent_tokenize(abstract)
    words = []
    for sent in sents:
        j += 1
        words.append(word_tokenize(sent))

    stop_words = set(stopwords.words('english'))

    g = open("../cut-to-token/{}.tsv".format(i),'w')
    a.write(str(j)+'\n')
    for sent in words:
        for word in sent:
            if word not in stop_words:
                g.write(word+'\n')
        g.write('\n')
    g.close()
a.close()