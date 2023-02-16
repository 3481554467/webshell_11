import jieba
import re
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.test.utils import common_texts

import gensim.downloader as api

f = open(r"D:\workSpace\webshell_Project\date\train\jspCode", 'r', encoding='utf-8')  # 读入文本
lines = []
for line in f:  # 分别对每段分词
    temp = jieba.lcut(line)  # 结巴分词 精确模式
    words = []
    for i in temp:
        # 过滤掉所有的标点符号
        i = re.sub("[\s+\.\!\/_,$%^*(+\"\'””《》]+|[+——！，。？、~@#￥%……&*（）：；‘]+", "", i)
        if len(i) > 0:
            words.append(i)
    if len(words) > 0:
        lines.append(words)

# model = Word2Vec(lines, vector_size=20, window=2, min_count=3, epochs=7, negative=10, sg=1)
# model.save('jspVec.model')

model = Word2Vec(lines, vector_size=100, window=2, min_count=3, epochs=7, negative=10, sg=1)
model.save('jspVec_vecsize100.model')