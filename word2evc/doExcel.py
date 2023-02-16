import csv
import os
file = r'D:\workSpace\webshell_Project\date\train.csv'

with open(file) as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

    list1 = []
    list2 = []
    for r in rows:
        if (r[1] == 'php'):
            list1.append(r[0])
        elif (r[1] == 'jsp'):
            list2.append(r[0])


import os

root = r'D:\workSpace\webshell_Project\date\train'
path = r'D:\workSpace\webshell_Project\date\train\train'
files = os.listdir(path)
result = os.path.join(root, 'result')  # 生成最终txt文件(result.txt)的路径
jspCode = os.path.join(root, 'jspCode')  # 生成最终txt文件(result.txt)的路径

if (os.path.exists(r'D:\workSpace\webshell_Project\date\train\jspCode'))==False:
    with open(jspCode, 'w', encoding='utf-8-sig') as r:
        for i in range(0, int((len(list2) - 1) * 0.8)):
            fname = str(list2[i])
            filename = os.path.join(path, fname)
            with open(filename, 'r', encoding='utf-8-sig') as f:
                for line in f:
                    r.writelines(line)
                r.write('\n')
