#!/usr/bin/env python3

import nltk

# 分词
text = "the little yellow dog barked at the cat"
sentence = nltk.word_tokenize(text)

# 词性标注
sentence_tag = nltk.pos_tag(sentence)
print(sentence_tag)

# 定义分块语法
# 这个规则是说一个NP块由一个可选的限定词后面跟着任何数目的形容词然后是一个名词组成
# NP(名词短语块) DT(限定词) JJ(形容词) NN(名词)
grammar = "NP: {<DT>?<JJ>*<NN>}"

# 进行分块
cp = nltk.RegexpParser(grammar)
tree = cp.parse(sentence_tag)
tree.draw()