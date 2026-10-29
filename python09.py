#lists in python

'''l1=[]
print(l1)
print(type(l1))'''

'''r=range(0,10)
l=list(r)
print(l)'''

'''l=[1,2,3,4,5]
print(l)
print("Before modifying l[0]: " , l[0])
l[0]=20
print("After modifying l[0]: ", l[0])
print(l)'''

'''a=[100,200,300,400]
x = 0
while x<len(a):
    print(a[x])
    x=x+1'''

'''a=[1,2,3,4,4,4,4,5,5,5,3,3]
print(a.count(3))
print(a.count(4))
print(a.count(5))'''

'''l=[]
l.append("Ramesh")
l.append("Suresh")
print(l)'''

'''l=[10,20,30,40]
l.insert(0,76) #where the element before the comma denotes the position in the list, starting from 0 or -5
print(l)'''

'''l=[10,20,30,40]
print(l)
l.insert(1,111)
print(l)
l.insert(-1,222)
print(l)
l.insert(10,233)
print(l)
l.insert(-10,444)
print(l)'''

'''l=[1,2,3,1]
l.remove(1)
print(l)

l=[4,2,3,1]
l.remove(1)
print(l)'''

#REMOVE:-removes element, gives value error
#POP: removes index, gives index error

'''n=[1,2,3,4,5]
print(n.pop(1))
print(n)
print(n.pop())
print(n)'''

'''n=[1,2,3,4,'two']
print(n)
n.reverse()
print(n)'''

#SORT(): should contain only homogenous elements.

'''n=[1,4,2,3,5]
n.sort()
print(n)
n=['SURESH', 'RAMESH', 'ARJUN']
n.sort()
print(n)'''

#CLONING:- copies the moemory as well as location
#SHALLOW COPY
'''x=[10,20,30]
y=x
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))'''

#DEEP/CLONING COPY
'''x=[10,20,30]
y=x.copy()
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))

x=[10,20,30]
y=x[:]
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))'''

#MATHEMATICAL OPERATOR ON LIST(+,*)
'''a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

a=[1,2,3]
b='BALLU'     #TYPE ERROR
c=a+b
print(c)'''

'''a=[1,2,3]
print(a)
print(2*a)'''

#COMAPRISON
'''print([1,2,3]<[2,2,3])
print([1,2,3]<[1,2,3])
print([1,2,3]<[1,2,4])
print([1,2,3]==[1,2,3])
print([1,2,3]==[1,2,4])'''

'''x=["abc","def","ghi"]
y=["abc","def","ghi"]
z=["ABC","DEF","GHI"]
print(x==y)
print(x==z)'''

#NESTED LISTS
'''l1=[1,2,3,[45,[55,67,[45]],90],56,5]
print(l1[3][1][2][0])

a=[80,90]
b=[10,20,30,a]
print(b[3][1])'''

#LAMBDA EXPRESSION

'''a=lambda x,y:x**y
print(a(4,3))

l1=[1,2,3,4,5,6]
f=filter(lambda x:x%3==0,l1) #selects elements from list that satisfy the condition
l=list(f)
print(l)
f=filter(lambda arun:arun%3==0,l1)
l2=list(f)
print(l2)
f=map(lambda i:i**2,l1) #puts the elements into the lamdba expression and gives output
l3=list(f)
print(l3)'''

'''l=[1,2,3,4,5,-3,77]
from functools import reduce
f=reduce(lambda x,y:x if x<y else y,l)
print(f)'''

#LIST COMPREHENSION
'''l1=[1,2,3,4,5,6,7,8]
l2=[x**2 for x in l1]
print(l2)
l3=[x for x in l1 if x%2]
print(l3)

s=range(1,20,3)
for i in s:
    print(i)
m=[x for x in s if x%2==0]    
print(m)'''
