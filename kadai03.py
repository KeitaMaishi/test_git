import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd

list1=["2014年度","2015年度","2016年度","2017年度","2018年度","2019年度"]
list2=[1452,1796,1894,2584,2735,3447]
list3=[3231,3747,3726,5853,8866,10913]
index1=['オープンキャンパス参加者数','志望者数']

data ={
    '年度':list1,
    'OC参加者数':list2,
    '志望者数':list3
}

df=pd.DataFrame(data)

plt.scatter(df['年度'],df['OC参加者数'])
plt.scatter(df['年度'],df['志望者数'])
plt.title("年度別オープンキャンパス参加者数と志望者数の推移")
plt.xlabel("年度")
plt.ylabel("人数")
plt.legend(index1,loc="upper left")
plt.show()
