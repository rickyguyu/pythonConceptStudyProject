
# -*- coding: cp936 -*-
import re
import linecache
import numpy as np
import os
 
filename = 'preprocess1.txt'
 
#��ֵ�ı��ļ�ת��Ϊ˫�б���ʽ[[...],[...],[...]],����̬��ά����
#Ȼ��˫�б���ʽͨ��numpyת��Ϊ���������ʽ
def txt_strtonum_feed(filename):
    data = []
    with open(filename, 'r') as f:#with����Զ�����close()����
        line = f.readline()
        while line:
            eachline = line.split()###���ж�ȡ�ı��ļ���ÿ���������б���ʽ����
            read_data = [ float(x) for x in eachline[0:7] ] #TopN�����ַ�ת��Ϊfloat��
            lable = [ int(x) for x in eachline[-1] ]#lableת��Ϊint��
            read_data.append(lable[0])
            #read_data = list(map(float, eachline))
            data.append(read_data)
            line = f.readline()
        return data #��������Ϊ˫�б���ʽ
 
#��ֵ�ı��ļ�ֱ��ת��Ϊ����������ʽ������
def txtfile2matrix(filename):
    file=open(filename)
    lines=file.readlines()
    #print lines
    #['0.94\t0.81\t...0.62\t\n', ... ,'0.92\t0.86\t...0.62\t\n']��ʽ
    numLines=len(lines)#�ļ�����
    numRows=len(lines[0].strip().split('\t'))
    
    dataMatrix=np.zeros((numLines,numRows))#��ʼ������
 
    currLine=0
    for line in lines:
        listLine=line.strip().split('\t')#strip()Ĭ���Ƴ��ַ�����β�ո���з�
        dataMatrix[currLine,:]=listLine[:]
        currLine+=1
 
    return dataMatrix
 
 
#��ֵ�ı��ļ�ֱ��ת��Ϊ����������ʽ������
def text_read(filename):
    # Try to read a txt file and return a matrix.Return [] if there was a mistake.
    try:
        file = open(filename,'r')
    except IOError:
        error = []
        return error
    content = file.readlines()
 
    rows=len(content)#�ļ�����
    datamat=np.zeros((rows,8))#��ʼ������
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
    #['0.94\t0.81\t...0.62\t\n', ... ,'0.92\t0.86\t...0.62\t\n']��ʽ
    rows=len(lines)#�ļ�����
 
    dataarray=np.zeros(rows)#��ʼ������
 
    row=0
    for line in lines:
        line=eval(line.strip()) #strip()Ĭ���Ƴ��ַ�����β�ո���з�
        dataarray[row]=float(line)
        row+=1
 
    return dataarray
 
 
if __name__ == '__main__':
 
    #test_content = txt_strtonum_feed('preprocess1.txt')
    #content = np.array(test_content)
    #print content #����������ʽ
    #print '\n'
    #print test_content #��ά�б�
 
    print(txtfile2matrix("data/privatetest.dat"))
    #print(txt_to_array("data/privatetest.dat"))
    
    
    #out = text_read('preprocess1.txt')
    #print out
