#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:30:27 2019

@author: frank-lsy
"""

import random

result_list = random.sample(range(1,301),300)
print(len(result_list))

train_set = result_list[0:240]
testa_set = result_list[240:270]
testb_set = result_list[270:300]

print(train_set)
print(testa_set)
print(testb_set)