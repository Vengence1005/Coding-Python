#Code 1
'''
from array import *
a=array("i",[1,3,5,7,9])
print (a)
'''
'''
#Code 2
from numpy import *
a = linspace(0,10,4)
print (a)

b = logspace(1,6,3)
print(b)

c = arange(1,30,8)
print(c)

d = zeros(7)
print(d)

e = ones(7)
print(e)
'''

#Code 3
'''
from array import *
a = array("i",[1,3,5,7,9])
b = array("i",[2,4,5,8,9])
c = []
d =[]
e=[]
for i in range(5):
    c.insert(i , a[i]==b[i])
    d.insert(i,  a[i] >=b[i])
    e.insert(i,  a[i]<=b[i])
print('Result of A<=B: ' , e)
print('Result of A==B: ' , c)
print('Result of A>B: ' , d)
'''
#Code 4
'''
from numpy import *
a = [2,4,6,8,10]
b = [2,0,6,0,10]
c = []
d =[]
e =[]
for i in range(5):
    c.insert(i,logical_and(a[i]>0 , a[i]<4))
    d.insert(i,logical_or( b[i]>0 , b[i]==6)) 
    e.insert(i,logical_not(b[1]))
print(c)
print(e)
print(d)
'''
#Code 6




































    





















