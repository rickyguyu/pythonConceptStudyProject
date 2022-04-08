# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:53:35 2020

@author: Ricky
"""



import pandas as pd
import numpy as np
a =pd.Series([9,8,7,6])
b =pd.Series([9,8,7,6],index=["a","b","c","d"])
b1 =pd.Series([9,8,7,6],index=["a","b","c","d"])
c =pd.Series(25,index=["a","b","c","d"])
d =pd.Series({"a":9,"b":8,"c":7})
e =pd.Series({"a":9,"b":8,"c":7},index=["c","a","b","d"]) # 通过字典建立Series,通过所需index排序
f =pd.Series(np.arange(5),index=np.arange(9,4,-1))
print(a)
print(b)
print(c)
print(d)
print(e)
print(e.get("f",100)) #如果没有f就返回100
print(f)
b1 =pd.Series([1,2,3,4],index=["c","d","e","f"])
print(b+b1) # Series 对象对齐，2个都有同样index的值相加，一个没有值，一个有值添加对象但值为NaN
e.name="试名字"
e.index.name="索引名"
e["b","d"]=20
print(e)

#  Dataframe
z=pd.DataFrame(np.arange(10).reshape(2,5))
print(z)  # Via Numpy nd  create DataFrame
dt={"one":pd.Series([1,2,3],index=["a","b","c"]),"two":b} 
df1=pd.DataFrame(dt) 
print(df1) # via Dict create Datefram
df2=pd.DataFrame(dt,index=["b","c","d"],columns=["two","three"]) 
print(df2) #via Dict create DataFrame select index and columns
d3={"one":[1,2,3,4],"two":[9,8,7,6]}
df3=pd.DataFrame(d3,index=["a","b","c","d"])
print(df3) #via Dict list create DataFrame

dt4={"城市":["北京","上海","广州","深圳","沈阳"],"环比":[101.5,101.2,101.3,102.0,100.1],"同比":[120.7,127.3,119.4,140.9,101.4],"定基":[121.4,127.8,120.0,145.5,101.6]}
df4=pd.DataFrame(dt4,index=["c1","c2","c3","c4","c5"])
#df4.index.name="城市"
print(df4)
print(df4["同比"]["上海"])
print(df4.loc["c2"]) # 取Dataframe的一个index * 同df4.ix["上海"] ix已不用
# 重新排列Index和Columns
df4.reindex(index=["c2","c1","c3","c4","c5"],columns=["城市","同比","环比","定基"])
# 增加一列
newc=df4.columns.insert(3,"新增")
df4.reindex(columns=newc,fill_value=200)
print(df4)
ac0 = df4.index.insert(5,"c0")
df4.reindex(index=ac0,method="bfill")
ac6 = df4.index.insert(6,"c6")
df4.reindex(index=ac6,method="ffill")
#删除Index axis=0
df4.drop("c5")
#删除Columns axis=1
df4.drop("定基", axis=1)

#行排序 axis =0
df4.sort_index()
df4.sort_index(ascending=False)
# 列排序 axis=1
df4.sort_index(axis=1)
df4.sort_index(axis=1,ascending=False)

#值排序 行排序 axis=0
df4.sort_values("同比")
df4.sort_values("同比",ascending=False)

#值排序 列排序 axis=1
df5 = df4.drop("城市",axis=1) #名字不能排序，要去掉以后再排序
df5.sort_values("c2",axis=1,ascending=False)
newcolumn=df5.columns.insert(0,"城市")
df5["城市"] =["北京","上海","广州","深圳","沈阳"] # 然后再加上此列
df5.reindex(columns=newcolumn)

#统计值
ana =pd.Series({"a":9,"b":8,"c":7},index=["a","b","c","d"])
print(ana.describe())
# 累计计算cumsum cumprod cummin cummax 上下行累计
# 滚动计算rolling(w).sum() .mean() .var()  .std() .min() .max() 上下行前w项到当前项，如果不到w则空
# 相关分析 协方差 Pearson相关系数 .cov() .corr()
hpricesIn = pd.Series([3.04,22.93,12.75,22.6,12.33], index=["2008","2009","2010","2011","2012"])
m2In = pd.Series([8.18,18.38,9.13,7.82,6.69], index=["2008","2009","2010","2011","2012"])
hpricesIn.cov(m2In)
hpricesIn.corr(m2In)
# hpricesIn.cov(m2In)
# Out[173]: 20.625449999999994

# hpricesIn.corr(m2In)
# Out[174]: 0.5239439145220387
# 有中等相关性


