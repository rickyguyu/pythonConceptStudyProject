# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 01:15:53 2020

@author: Ricky
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

def firstpic():
    plt.plot([0,2,4,6,8],[3,1,4,5,2])
    plt.ylabel("Grade")
    plt.axis([-1,10,0,6])
    # plt.savefig("pltpic1",dpi=600)
    plt.show()

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def secondpic() :
    a = np.arange(0.0,5.0,0.02)
    plt.subplot(211)
    plt.plot(a,f(a),"-")
    plt.subplot(212)
    plt.plot(a,np.cos(2*np.pi*a),"r--")

# 显示中文
def thirdpic():
    #matplotlib.rcParams["font.family"]="SimHei" #定义全局字体
    plt.plot([0,2,4,6,8],[3,1,4,5,2])
    plt.ylabel("纵轴（值）",fontproperties="SimHei") #定义局部字体
    plt.xlabel("横轴（值）",fontproperties="SimHei") #定义局部字体
    plt.axis([-1,10,0,6])
    # plt.savefig("pltpic1",dpi=600)
    plt.show()
    
    
def fourthpic():
    #y=x**2 图形绘制
    x= np.linspace(-100,100,10)
    # x=np.arange(100)
    # x= np.random.randint(1,100,(3,4)).flatten()
    
    plt.subplot(221)
    #plt.subplot2grid((2,2),(0,0),colspan=2)
    plt.title("y = x^2")
    plt.plot(x,x**2,"r-.")
    plt.ylabel("y（值）",fontproperties="SimHei") #定义局部字体
    plt.xlabel("x（值）",fontproperties="SimHei") #定义局部字体
    plt.annotate(r"x = 2",xy=(2,4), xytext=(25,7500),arrowprops=dict(facecolor="black",shrink=0.1,width=0.1))
    plt.axis([-100,100,0,10000])
    
    x1= np.linspace(1,100,10)
    plt.subplot(224)
    #plt.subplot2grid((2,2), (1,0), colspan=2)
    
    plt.title("y = log10(x)")
    plt.plot(x1,np.log10(x1),"g--")
    plt.ylabel("y（值）",fontproperties="SimHei") #定义局部字体
    plt.xlabel("x（值）",fontproperties="SimHei") #定义局部字体
    plt.annotate(r"x = 2",xy=(40,1.5), xytext=(40,0.5),arrowprops=dict(facecolor="black",shrink=0.1,width=0.1))
    plt.axis([0,100,0,2])
    
def fifthpic():
    lables = "Frogs","Hogs","Dogs","Logs"
    size =([15,30,45,10])
    explode=(0,0.1,0,0)
    plt.pie(size,explode,lables,autopct="%1.1f%%",shadow=False,startangle=90)
    plt.show()
    
def sixthpic():
    np.random.seed(0)
    mu,sigma = 100,20
    a= np.random.normal(mu,sigma,size=100)
    plt.hist(a,100,histtype="stepfilled",alpha=0.75)
    plt.show()
    
def seventhpic(): # 散点图面向对象方法
    matplotlib.rcParams["font.family"]="Arial" #定义全局字体
    fig, ax = plt.subplots()
    ax.plot(10*np.random.randn(100),10*np.random.randn(100),".")
    plt.show()

if __name__ =="__main__":
   #  firstpic()
    secondpic()
   # thirdpic()
   # fourthpic()
   # fifthpic() 
   # sixthpic()
   #seventhpic()
