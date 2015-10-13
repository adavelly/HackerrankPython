'''
Created on Oct 13, 2015

@author: user
'''
arr = []
N=int(raw_input())
for i in range(N):
    inputcommand=raw_input()
    c=inputcommand.split(" ")
    if c[0]=='insert':
        arr.insert(int(c[1]),int(c[2]))
    elif c[0]=='remove':
        arr.remove(int(c[1]))
    elif c[0]=='pop':
        arr.pop()
    elif c[0]=='append':
        arr.append(int(c[1]))
    elif c[0]=='extend':
        arr.extend(int(c[1]),int(c[2]))
    elif c[0]=='index':
        arr.index(int(c[1]))
    elif c[0]=='count':
        arr.count(int(c[1]))
    elif c[0]=='sort':
        arr.sort()
    elif c[0]=='reverse':
        arr.reverse()
    elif c[0]=='print':
        print arr