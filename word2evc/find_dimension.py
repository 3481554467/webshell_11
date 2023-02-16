import re
import numpy
from doExcel import list2
import jieba
from gensim.models import Word2Vec
myList=[]
root = "D:/workSpace/webshell_Project/date/train/train/"


def getWordNum(fileNumber):
    sentence =[]
    filepath = root + str(fileNumber)
    f = open(filepath, 'r', encoding='utf-8')
    lines = []
    for line in f:  # 分别对每段分词
        temp = jieba.lcut(line)  # 结巴分词 精确模式
        words = []
        for i in temp:
            i = re.sub("[\s+\.\!\/_,$%^*(+\"\'””《》]+|[+——！，。？、~@#￥%……&*（）：；‘]+", "", i)
            if len(i) > 0:
                words.append(i)
        if len(words) > 0:
            lines.append(words)

    return len(lines[0])

for index in list2:
    print(index)
    myList.append(getWordNum(index))

numpy.save("myList_wordNum.npy",myList)



