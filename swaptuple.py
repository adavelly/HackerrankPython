'''
Created on Oct 12, 2015

@author: user
'''
i=int(raw_input())
j=int(raw_input())
a=(i,j)
temp1=a[0]
temp2=a[1]
temp=temp2
temp2=temp1
temp1=temp
print(temp1)
print(temp2)