'''a=10
b=20
c=30
d=40'''
#t=a,b,c,d tupple packing 
#d,c,b,a=t tuple unpacking

#SINGLE VALUE
'''SINGLE VALUE TUUPLE NEED A COMMA(,) TO IDENTIFY STR OR INT AS A TUPPLE'''
'''a=("SUSHANT")
print(a)
print(type(a))
a=("SUSHANT",)
print(a)
print(type(a))
b=(2)
print(b)
print(type(b))
b=(2,)
print(b)
print(type(b))'''

"""t1=(10,20,30) #CONCATENATION
t2=(40,50,60)
t3=t1+t2
print(t3)
t4=t1*3
print(t4)"""

'''t=(10,20,10,10,20)
print(t.index(10))
print(t.index(30))''' #VALUE ERROR

#SORTED
#IN ASCENDING 
#IN DESCENDING

'''t=(40,10,30,20)
t1=sorted(t)
print(t)
print(t1)
t2=sorted(t,reverse=True)
print(t2)
t3=t1[::-1]
print(t3)'''

#TUPPLE PACKING
'''l=[]
for x in range(3):
    roll=int(input("Enter roll no. : "))
    name=input("Enter name: ")
    email=input("Enter email: ")
    phone=input("Enter Phone: ")
    t=roll,name,email,phone #TUPLE PACKING
    l.append(t)
for r,n,e,p in l: #TUPPLE UNPACKING
    print("%5d %-15s %-20s %10s"%(r,n,e,p))'''

#COMPREHENSION
'''t=(x**2 for x in range(1,6))
print(type(t))
for x in t:
    print(x)'''

#MIN AND MAX DOUBT



