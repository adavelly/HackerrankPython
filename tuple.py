'''
Created on Oct 13, 2015

@author: user
'''
N=int(raw_input())
inputstring=raw_input()
inputtuple=inputstring.strip().split()
if len(inputtuple)==N:
    print hash(tuple(map(int,inputtuple)))