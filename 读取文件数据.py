
# -*- coding: cp936 -*-
import re
import linecache
import numpy as np
import os
 
filename = 'preprocess1.txt'
 
#数值文本文件转换为双列表形式[[...],[...],[...]],即动态二维数组
#然后将双列表形式通过numpy转换为数组矩阵形式
def txt_strtonum_feed(filename):
    data = []
    with open(filename, 'r') as f:#with语句自动调用close()方法
        line = f.readline()
        while line:
            eachline = line.split()###按行读取文本文件，每行数据以列表形式返回
            read_data = [ float(x) for x in eachline[0:7] ] #TopN概率字符转换为float型
            lable = [ int(x) for x in eachline[-1] ]#lable转换为int型
            read_data.append(lable[0])
            #read_data = list(map(float, eachline))
            data.append(read_data)
            line = f.readline()
        return data #返回数据为双列表形式
 
#数值文本文件直接转换为矩阵数组形式方法二
def txtfile2matrix(filename):
    file=open(filename)
    lines=file.readlines()
    #print lines
    #['0.94\t0.81\t...0.62\t\n', ... ,'0.92\t0.86\t...0.62\t\n']形式
    numLines=len(lines)#文件行数
    numRows=len(lines[0].strip().split('\t'))
    
    dataMatrix=np.zeros((numLines,numRows))#初始化矩阵
 
    currLine=0
    for line in lines:
        listLine=line.strip().split('\t')#strip()默认移除字符串首尾空格或换行符
        dataMatrix[currLine,:]=listLine[:]
        currLine+=1
 
    return dataMatrix
 
 
#数值文本文件直接转换为矩阵数组形式方法三
def text_read(filename):
    # Try to read a txt file and return a matrix.Return [] if there was a mistake.
    try:
        file = open(filename,'r')
    except IOError:
        error = []
        return error
    content = file.readlines()
 
    rows=len(content)#文件行数
    datamat=np.zeros((rows,8))#初始化矩阵
    row_count=0
    
    for i in range(rows):
        content[i] = content[i].strip().split('\t')
        datamat[row_count,:] = content[i][:]
        row_count+=1
 
    file.close()
    return datamat


def txt_to_array(filename):
    file=open(filename)
    lines=file.readlines()
    #print lines
    #['0.94\t0.81\t...0.62\t\n', ... ,'0.92\t0.86\t...0.62\t\n']形式
    rows=len(lines)#文件行数
 
    dataarray=np.zeros(rows)#初始化数组
 
    row=0
    for line in lines:
        line=eval(line.strip()) #strip()默认移除字符串首尾空格或换行符
        dataarray[row]=float(line)
        row+=1
 
    return dataarray
 
 
if __name__ == '__main__':
 
    #test_content = txt_strtonum_feed('preprocess1.txt')
    #content = np.array(test_content)
    #print content #矩阵数组形式
    #print '\n'
    #print test_content #二维列表
 
    print(txtfile2matrix("data/privatetest.dat"))
    #print(txt_to_array("data/privatetest.dat"))
    
    
    #out = text_read('preprocess1.txt')
    #print out
