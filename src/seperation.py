# this program is aimed at seperating the datasets in S2S project
# the original data's texture form is like: abc. /t def.
# the processed data's texture form is like
# .en: abc.    .zh: def

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@file: seperation.py
@time: 2019/12/5
@desc: seperating the training(or testing) text data which contains both source language and target language into 2 seperated text files
each of them contains only one language。
"""
import sys
import os
import math
from torchtext import data


def seperation(path_cin, path_cout1, path_cout2, **kwargs):
    examples = []
    text_en = []
    text_zh = []
    print('loading dataset from {}'.format(path_cin))
    with open(path_cin, encoding="utf-8-sig") as f:
        for line in f.readlines():
            src = line.split("\t")[0]
            trg = line.split("\t")[1].replace("\n", "")
            trg = trg[::-1]
            text_en.append(src)
            text_zh.append(trg)
        
    with open(path_cout1,'w') as en, open(path_cout2, 'w') as zh:
        for line_en, line_zh in zip(text_en, text_zh):
            en.write(line_en + '\n')
            zh.write(line_zh + '\n')
    f.close()
    en.close()
    zh.close()

cin_path = "train1.txt"
cout_en_path = "train.en"
cout_zh_path = "train.zh"

seperation(cin_path, cout_en_path, cout_zh_path)

