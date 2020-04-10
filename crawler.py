# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:03:12 2020

@author: user
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

B=[]
F=[]
D=[]
G=[]
I=[]


url = "https://evertrust.yungching.com.tw/region/%e5%8f%b0%e5%8d%97%e5%b8%82/%e4%b8%8d%e9%99%90/1?t=2,3,4,5&a=&c=#mainContent"
for i in range(2,101): #往上爬3頁
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select("td.dealPrice text") #標題
    #floor = soup.select("td.floorSpace")
    plot = soup.select("td.plot")
    ty = soup.select("td.type")
    
    park = soup.select("td.parkingSpace")
    
    #print ("本頁的URL為"+url)
    url = "https://evertrust.yungching.com.tw/region/%e5%8f%b0%e5%8d%97%e5%b8%82/%e4%b8%8d%e9%99%90/"+ str(i) +"?t=2,3,4,5&a=&c=#mainContent"
    
    for s in sel:        
        A=(s.text).replace(',','')
        B.append((A).replace('萬',''))
   
    for p in plot:
        F.append((p.text).replace('坪',''))
      
    for i in ty:        
        A=(i.text).replace('公寓','0')
        A=A.replace('套房','1')
        A=A.replace('透天厝','2')
        D.append(A.replace('店面','3'))
        
    
    
    for i in park:
        A=(i.text).replace('無','0')
        I.append(A.replace('有','1'))
        
   

url1 = "https://evertrust.yungching.com.tw/print/region/%e5%8f%b0%e5%8d%97%e5%b8%82/%e4%b8%8d%e9%99%90/1?t=2,3,4,5&a=&c="
for i in range(2,101): 
    r = requests.get(url1)
    soup1 = BeautifulSoup(r.text,"html.parser")
     
    uprice = soup1.select("td.red")
    #print ("本頁的URL為"+url)
    url1 = "https://evertrust.yungching.com.tw/print/region/%e5%8f%b0%e5%8d%97%e5%b8%82/%e4%b8%8d%e9%99%90/"+ str(i) +"?t=2,3,4,5&a=&c="
    
    
        
    for i in uprice:
            
        G.append((i.text).replace('萬',''))    

dataframe = pd.DataFrame({'Type':D,'Final Price':B,'Unit Price':G,'Flooring':F,'Parking Space':I})
dataframe.to_csv("House.csv",index=False,sep=',',encoding='utf_8_sig')    
