import re
import sys,os
from os import path
address = sys.argv[1]
address = sys.argv[1].replace('\\','\\\\')
pwd = os.getcwd()
pwd = pwd.replace('\\','\\\\')
out_address = pwd + '\\\\out-result.txt'
f1 = open(address,'r')
f2 = open(out_address,'w+')
count = 0
key_word = input("输入关键字： ")
for line in f1.readlines():
    if re.findall(key_word ,line):
        line = line.replace("[Text][Motors|motor2|", "[Linear][")

        # print(line1)
    f2.write(line) 
f1.close()
f2.close()
print("找到的行数：",count)
os.system("pause")