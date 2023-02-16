import numpy

jspList = numpy.load("jsplist_PCA_sourcecode.npy",allow_pickle=True)
print(len(jspList))
print(jspList)
jspList1 = jspList[:2146]#用于训练的jsp文件
print(len(jspList1))
from xgboost import XGBClassifier

jspLable = []

import csv

file = r'D:\workSpace\webshell_Project\date\train.csv'

with open(file) as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

    list1 = []
    list2 = []
    for r in rows:
        if (r[1] == 'jsp'):
            if (r[2] == 'white'):
                jspLable.append(0)
            elif (r[2] == 'black'):
                jspLable.append(1)

jspLable1 = jspLable[:2146]
print(len(jspLable))
print(jspLable)

# model = XGBClassifier(max_depth=8, min_child_weight=1, learning_rate=0.1, n_estimators=1000, gamma=0)
model = XGBClassifier(max_depth=20, min_child_weight=1, learning_rate=0.01, n_estimators=2000, gamma=0)
model.fit(jspList1, jspLable1)


# print(jspList[2682])
# print(model.predict([[-0.46731662,  0.31526311, -0.163543,   -0.28638706,  0.4844007 ,  0.16305707,
#  -0.05450008 , 1.01005828 ,-0.58344436, -0.11138322 , 0.2877445,  -0.71594841,
#  -0.43534168 ,-0.41041721,  0.14583903,  0.01629745 , 0.87842234 ,-0.44111353,
#  -0.49414957 , 0.27512625]]))






def predict():
    TP = 0
    FN = 0
    TN = 0
    FP = 0
    right = 0
    false = 0
    with open(file) as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

        index = 0
        for r in rows:
            if r[1] == 'jsp':
                # print("ee")

                if index < 2145:
                    index = index + 1
                    # print("ee")

                elif 2145<=index<2682:
                    #print("ee")
                    vec = jspList[index]

                    vec1 = list(vec)
                    result = model.predict([vec1])
                    # if result == jspLable[index]:
                    #     right = right + 1
                    # else:
                    #     false = false + 1
                    # index=index+1
                    # print(jspLable[index])
                    # print(result)
                    if jspLable[index]==0 and result ==0 :
                        TP=TP+1
                    elif jspLable[index]==0 and result ==1:
                        FN=FN+1
                    elif jspLable[index] == 1 and result == 0:
                        FP = FP + 1
                    elif jspLable[index]==1 and result ==1:
                        TN=TN+1
                    index=index+1

    return TP,FN,FP,TN

TP,FN,FP,TN=predict()
print("TP=",TP)
print("FN=",FN)
print("FP=",FP)
print("TN=",TN)

accuracy=(TP+TN)/(TP+TN+FP+FN)
precision=TP/(TP+FP)
recall=TP/(TP+FN)
F1=(2*precision*recall)/(precision+recall)

print("accuracy=",accuracy)
print("precision=",precision)
print("recall=",recall)
print("F1=",F1)


