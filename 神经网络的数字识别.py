import numpy as np
from os import listdir
from sklearn.neural_network import MLPClassifier

def img2vector(filename):
	retMat = np.zeros([1024],int)
	fr = open(filename)
	lines = fr.readlines()
	for i in range(32):
		for j in range (32):
			retMat[i*32+j] = lines[i][j]
	return retMat

def read DataSet(path):
	fileList = listdir(path)
	numFiles = len(fileList)
	dataSet = np.zeros([numFiles,1024],int)
	hwLabels = np.zeros([numFiles,10])
	for i in range(numFiles):
		filePath = fileList[i]
		digit = int(filePat.split("_")[0])
		hwLabels[i][digit] = 1.0
		dataSet[i] = img2vector(path+"/"+filePath)
	return dataSet,hwLabels
	