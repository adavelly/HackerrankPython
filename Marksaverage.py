'''
Created on Oct 12, 2015

@author: user
'''
from __future__ import division
N=int(raw_input())
student ={}
p=0
temp=0
for i in range(N):
    c=raw_input()
    student[i]=c.split()
Searchname=raw_input()
for i in range(N):
    if(Searchname==student[i][0]):
        temp=i
p=0
sumof=0
n=len(student[temp])
while p<n-1:
    p=p+1
    sumof+=float(student[temp][p])
print("{0:.2f}".format(sumof/(n-1)))