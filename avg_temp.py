# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 20:12:34 2023

@author: TULIKA
"""

cityTemp=open('citytemp.csv','r')
rec1=cityTemp.readline()
c,t,d=rec1.split(',')
prev=c;
sum=0.0;
count=0;

cityTemp.seek(0)

for record in cityTemp:
    record=record.rstrip('\n')
    city,temp,degree=record.split(',')
    if degree=="C":
        temp=(float(temp)*9/5)+32
    if prev!=city:
        avg=sum/count
        print(prev+" "+str(avg))
        sum=0
        count=0
    sum+=float(temp)
    count+=1
    prev=city
print(prev+" "+ str(sum/count))  
        
         
    