#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:27:57 2019

@author: frank-lsy
"""

import pandas as pd
import random

def create_vocab(dir_in,vocab_file_out,sample_ids):
    file_vocab = open(vocab_file_out,'w')
    tmp_list = []
    for i in sample_ids:
        print(i)
        tmp = pd.read_csv('{}/{}.tsv'.format(dir_in,i+1),sep='\t',header=0)
        token = tmp['token']
        token.fillna('',inplace=True)
        for j in range(len(token)):
            if (token[j] != ''):
                line = token[j]+'\n'
                tmp_list.append(line)
                #file_vocab.write(line)
    new_list = list(set(tmp_list))
    for token in new_list:
        file_vocab.write(token)
    file_vocab.close()
    
def create_words_tags_dir(dir_in,words_file_out,sample_ids,header):
    file_words = open(words_file_out,'w')
    for i in sample_ids:
        print(i)
        tmp = pd.read_csv('{}/{}.tsv'.format(dir_in,i+1),sep='\t',header=0)
        token = tmp[header]
        token.fillna('\r',inplace=True)
        for j in range(len(token)):
            file_words.write(token[j]+' ')
        file_words.write('\n')
    file_words.close()

def create_words_tags_file(file_in,words_file_out,header):
    file_words = open(words_file_out,'w')
    tmp = pd.read_csv(file_in,sep='\t',header=0)
    token = tmp[header]
    token.fillna('\r',inplace=True)
    for j in range(len(token)):
        file_words.write(token[j]+' ')
    file_words.close()



result_list = random.sample(range(1,301),300)
print(len(result_list))

train_set = result_list[0:240]
testa_set = result_list[240:270]
testb_set = result_list[270:300]

dir_in = "../labeled-token"

words_file_out = "../virus/train.words.txt"
tags_bieo_out = "../virus/train.tags.txt"

testa_file_out = "../virus/testa.words.txt"
testb_file_out = "../virus/testb.words.txt"
testa_tags_bieo_out = "../virus/testa.tags.txt"
testb_tags_bieo_out = "../virus/testb.tags.txt"

header_token = 'token'
header_iob2 = 'IOB2'
header_bieo = 'BIEO'

#train
create_words_tags_dir(dir_in,words_file_out,train_set,header_token)
create_words_tags_dir(dir_in,tags_bieo_out,train_set,header_bieo)
#testa
create_words_tags_dir(dir_in,testa_file_out,testa_set,header_token)
create_words_tags_dir(dir_in,testa_tags_bieo_out,testa_set,header_bieo)
#testb
create_words_tags_dir(dir_in,testb_file_out,testb_set,header_token)
create_words_tags_dir(dir_in,testb_tags_bieo_out,testb_set,header_bieo)
