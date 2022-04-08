import numpy as np

#basic operation
print("5+6=",5+6)
print("3/2=",3/2)
print("3-2=",3-2)
print("5*8=",5*8)
print("2^6=",2**6)

# logistic operation
print("1==2:",1==2)
print("1!=2:",1!=2)
print("True & False:",  True & False)
print("True | False:",  True | False)
print("True xor False:",True ^ False)

# variable operation
a=3     #数值
b="hi"  #字符串
c=np.pi #浮点数PI
print(a,b)
print("PI的值是:%0.5f" %c) #注意print在浮点数替代的用法，中间是空格

# matrix operation
import numpy.matlib
print (np.matlib.empty((2,2)))  # 随机矩阵
print (np.matlib.rand(3,3))     # 0-1随机矩阵
print (np.matlib.randn(3,3))     # 负随机矩阵

# 特殊矩阵
print (np.matlib.zeros((2,2)))
print (np.matlib.ones((2,2)))

print (np.matlib.eye(n=3))
print (np.matlib.identity(5))

#自定义矩阵
i = np.matrix('1,2;3,4;5,6')  
print (i)

i = np.matrix('1,2,3')  
print (i)

i = np.matrix('1;2;3')  
print (i)

# 矩阵和多维数组转换
i = np.matrix('1,2;3,4;5,6')  
j = np.asarray(i)
print(j)                        # J为多维数组
k = np.asmatrix (j)  
print (k)                       # K为矩阵


#array operation
print(np.empty([3,2]))      # 创建随机多维数组


x = np.arange(5)          # 创建从0到5的步长为1的数组，注意不包含最后一个5
print (x)
x = np.arange(1,2,0.1)    # 创建从1到2的步长为0.1的数组，注意不包含最后一个2
print (x)
x = np.arange(1,6)        # 创建从1到6的步长为1的数组，注意不包含最后一个6
print (x)

a = np.linspace(1,2,11)   # 创建从1到2的步长为0.1的等差数组，包含最后一个2
print(a)

b = np.linspace(1,6,6)   # 创建从1到2的步长为0.1的等差数组，包含最后一个2
print(b)

# 数列和多维数组转换
x =  [1,2,3] 
a = np.asarray(x)  
print (a)
# 元组数列和多维数组转换
x =  (1,2,3) 
a = np.asarray(x)  
print (a)



#calculate matrix 矩阵和常数运算
print (2*np.matlib.ones((2,2)))
print (-6 + numpy.sqrt(10)*np.matlib.rand((1,3)))

w = -6 + numpy.sqrt(10)*np.matlib.rand((1,50))


#move matrix data
a = np.matrix('1,2;3,4;5,6')
print(a.size)
print(a.shape)
b = a.shape
np.asmatrix(b).shape
print("行数:", a.shape[0])
print("列数:", a.shape[1])
b= np.asarray([1,2,3,4,5])
print(b.size)

#读取数据文件
def loadMatrix(filename):
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

#自定义函数读取
print(loadMatrix("data/privatetest.dat"))
# loadtxt函数读取
my_matrix = numpy.loadtxt(open("data/privatetest.dat","rb"),delimiter="\t",skiprows=0)
print(my_matrix)

#存储Matrix变量到数据文件
a= loadMatrix("data/privatetest.dat")
b=a[2,1:3]       # 取a的第三行从第二列到第三列(不包含第三列) 
b1=np.asmatrix(b)
numpy.savetxt("data/my_matrix.dat",b1, delimiter = "\t")

#取matrix的特殊位置
print(a[[0,2],:]) #取a的第一行和第三行的所有数据a[[0,2],:]
#存matrix的特殊位置
a[:,2]=[10,11,12] #赋值a的第二列的所有数据
print(a)         


#合并矩阵
b=np.array([0,0,0])
c=np.row_stack((a,b)) #合并行
c=np.delete(c,3,0) #删除C的第4行
c=np.column_stack((a,b.T)) #合并列
c=np.delete(c,3,1) #删除C的第4列

d=np.ravel(c) #按行优先转成1维数组
print(d)
d=np.ravel(c,"F") #按列优先转成1维数组
print(d)

# 乘法操作
A = np.matrix('1,2;3,4;5,6')
B = np.matrix('11,12;13,14;15,16')
C = np.matrix('1,1;2,2')
print(A*C)  # same np.dot(A,C) 矩阵乘法
print(np.multiply(A,B)) # 每个元素相乘
# 每个元素计算要用array
np.asarray(A)* np.asarray(B)
np.asmatrix(np.asarray(A)**2) 
np.asmatrix(1/np.asarray(A))
np.log(np.asarray(A))
np.exp(np.asarray(A))
np.abs(np.asarray(A))
A.T #转换矩阵
A.I # 反矩阵

print(A.max(axis=0))  # 行最大值的数值 结果为 [5 6]
print(A.max(axis=1))  # 列最大值的数值结果为 [2 4 6]
print(A.argmax(axis=1)) # 所有列最大值元素所在的位置
print(A.argmax(axis=0)) # 所有行最大值元素所在的位置

3 > np.asarray(A) #每个元素判断返回逻辑值

A.sum()
A.sum(0)
A.sum(1)
A.prod()
A.prod(0)
A.prod(1)

np.floor(A)
np.ceil(A)
A1 =np.matlib.rand(3*3)
A2 =np.matlib.rand(3*3)
np.maximum(A1,A2) # 每个元素逐一比较取最大值

# 验证Magic矩阵的横竖斜都相同

a = np.matrix("8,1,6;3,5,7;4,9,2")
b= np.matlib.eye(n=3)
b1= np.flipud(b)
c= np.asarray(a)* np.asarray(b)
d= np.asarray(a)* np.asarray(b1)
a.sum(0)  #横等于15
a.sum(1)  #竖等于15
c.sum() # 正斜方向等于15
d.sum() # 反斜方向等于15


import matplotlib.pyplot as plt
# w = -6 + numpy.sqrt(10)*np.matlib.rand((1,50))
# plt.hist(w,bins=20)
# plt.show()
x = np.arange(0,0.98,0.01)
y = np.sin(2*np.pi*4*x)

y1=np.cos(2*np.pi*4*x)
plt.plot(x,y)
plt.plot(x,y1,"r")
plt.ylabel("Time") 
plt.xlabel("Value")
plt.axis([0,1,-1,1])
plt.legend(("sin","cos"),loc=1)
plt.title("My plot")
plt.savefig("myplot.png",dpi=600)
plt.show()

plt.subplot(221); plt.imshow(a)
plt.subplot(222); plt.imshow(a, cmap ='gray')
plt.subplot(223); plt.imshow(a, cmap = plt.cm.gray)
plt.subplot(224); plt.imshow(a, cmap = plt.cm.gray_r)
plt.colorbar()
plt.show()      #imagesc(a) 深浅颜色对比








