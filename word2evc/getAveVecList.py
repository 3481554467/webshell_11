import numpy
from gensim.models import Word2Vec
from doExcel import list2
import jieba
import re
from sklearn.decomposition import PCA

word_vectors = Word2Vec.load(r'D:\workSpace\webshell_Project\word2evc\jspVec_vecsize100.model')

# 得到了所有的词向量，接下来要对每一个文件操作，遍历所有单词，对所有单词之和取平均，作为这个样本的特征向量，存放到一个列表中,定义一个函数用来操作每一个文件并将其得到的结果(特征向量)append到featureVecList中
root = "D:/workSpace/webshell_Project/date/train/train/"


# def getAverageVec(fileNumber):
#     filepath = root + str(fileNumber)
#     f = open(filepath, 'r', encoding='utf-8')
#     lines = []
#     for line in f:  # 分别对每段分词
#         temp = jieba.lcut(line)  # 结巴分词 精确模式
#         words = []
#         for i in temp:
#             i = re.sub("[\s+\.\!\/_,$%^*(+\"\'””《》]+|[+——！，。？、~@#￥%……&*（）：；‘]+", "", i)
#             if len(i) > 0:
#                 words.append(i)
#         if len(words) > 0:
#             lines.append(words)
#
#     aveVec = numpy.zeros(100, dtype=float)
#     sum = 0
#     for word in lines[0]:
#         if word in word_vectors.wv.index_to_key:
#             aveVec += word_vectors.wv[word]
#             sum = sum + 1
#
#     aveVec = aveVec / sum
#     return aveVec

#输入文件名（数字号），输出sentence,即dXn的矩阵，之后再放入sent_PCA处理
def getSentence(fileNumber):
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

    for word in lines[0]:
        if word in word_vectors.wv.index_to_key:
            sentence.append(word_vectors.wv[word])

    return sentence
#
#
# def sent_PCA(sentence, n = 2):
#     sentence = numpy.array(sentence)
#
#     #print(sentence.shape)
#     pca = PCA(n_components = n)
#     #对每一个句子进行模型fit
#     pca.fit(numpy.array(sentence).transpose())
#     #pca.fit(np.array(sentence))
#     sentence = pca.transform(sentence.transpose())
#     #print(sentence.shape)
#     #返回所保留成分各自的方差百分比
#     variance = numpy.array(pca.explained_variance_ratio_)
#     #print("variance=",variance)
#     words = []
#     sentence = sentence.transpose()
#     #进行n次循环
#     for _ in range(n):
#         #抽取出最大值的下标
#         idx = numpy.argmax(variance)
#         # print("idx=",idx)
#         # print("np.amax(variance)",np.amax(variance))
#         # print(sentence.shape)
#         # print(sentence[idx].shape)
#         # print("sentence[idx]=",sentence[idx])
#         words.append(numpy.amax(variance) * sentence[idx])
#         variance[idx] = 0
#     return numpy.sum(words, axis = 0)


def sent_PCA(sentence, n = 2):
    pca = PCA(n_components = n)
    pca.fit(numpy.array(sentence).transpose())
    variance = numpy.array(pca.explained_variance_ratio_)
    words = []
    for _ in range(n):
        idx = numpy.argmax(variance)
        words.append(numpy.amax(variance) * sentence[idx])
        variance[idx] = 0
    return numpy.sum(words, axis = 0)


jspList = []
#
# for index in list2:
#     sentence=getSentence(index)
#     #sentence=sent_PCA(sentence)
#     print(index)
#     jspList.append(sentence)

for index in list2:
    sentence=getSentence(index)
    sentence=sent_PCA(sentence)
    print(index)
    jspList.append(sentence)



print(len(jspList))
#numpy.save("jsplist.npy", jspList)
#numpy.save("jsplist_withNoPCA.npy", jspList)
numpy.save("jsplist_PCA_sourcecode.npy", jspList)
#jsplist存储了所有jsp文件降维后的句向量，总共2683个


# phpList = []
# for index in range(len(list1)):
#     phpList.append(getAverageVec(list1[index]))
#
# numpy.save("phplist.npy", phpList)