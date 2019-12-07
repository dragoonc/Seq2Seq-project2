#!/usr/bin/env python
# -*- coding: UTF-8-sig -*-
# coding=gb18030 

"""
@file: vocab.py
@time: 2019/12/4
@desc: Assigning a number to each word according to the word frequency sequence, and then save the vocabulary to a separate vocab file.
"""

import codecs
import collections
from operator import itemgetter


def pre_vocab(lan):
    # 训练集数据文件
    ROOT_PATH = ""
    if lan == "zh":
        RAW_DATA = ROOT_PATH + "train.zh"
        # 输出的词汇表文件
        VOCAB_OUTPUT = ROOT_PATH + "zh.vocab"
        # 中文词汇表单词个数
        VOCAB_SIZE = 4000
    elif lan == "en":
        RAW_DATA = ROOT_PATH + "train.en"
        VOCAB_OUTPUT = ROOT_PATH + "en.vocab"
        VOCAB_SIZE = 10000
    else:
        print("wrong input")

    # 统计单词出现的频率
    counter = collections.Counter()
    with codecs.open(RAW_DATA, "r", "gb18030") as f:
        for line in f:
            for word in line.strip().split():
                counter[word] += 1

    # 按照词频顺序对单词进行排序
    sorted_word_to_cnt = sorted(counter.items(), key=itemgetter(1), reverse=True)
    sorted_words = [x[0] for x in sorted_word_to_cnt]

    # 在后面处理机器翻译数据时，出了"<eos>"，还需要将"<unk>"和句子起始符"<sos>"加入
    # 词汇表，并从词汇表中删除低频词汇。
    sorted_words = ["<unk>", "<sos>", "<eos>"] + sorted_words
    if len(sorted_words) > VOCAB_SIZE:
        sorted_words = sorted_words[:VOCAB_SIZE]

    with codecs.open(VOCAB_OUTPUT, 'w', 'utf-8') as file_output:
        for word in sorted_words:
            file_output.write(word + "\n")


if __name__ == "__main__":
    # 处理的语言
    lan = ["zh", "en"]
    for i in lang:
        pre_vocab(i)
