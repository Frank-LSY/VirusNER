#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 08:05:23 2019

@author: frank-lsy
"""

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

for i in range(300):
	f = open("../abstracts/human-neck-virus/{}.txt".format(i+1),'r')
	abstract = f.read()
	abstract.replace("\n","")
#print (abstract)
#print(word_tokenize(abstract))
	sents = sent_tokenize(abstract)
	mid_sents = ''
	words = []

	for sent in sents:
		words.append(word_tokenize(sent))
#print(words)

	stop_words = set(stopwords.words('english'))

	g = open("../cut-to-token/{}.tsv".format(i+1),'w')

#filtered_sents = []
	for sent in words:
    #filtered_words = []
		for word in sent:
			if word not in stop_words:
				g.write(word+'\n')
            #filtered_words.append(word)
		g.write('\n')
    #filtered_sents.append(filtered_words)
	g.close()
