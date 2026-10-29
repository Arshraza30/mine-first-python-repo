'''d={}
d[1]="RAMESH"
d[2]="SURESH"
d[3]="MITHILESH"
print(d)
print(d[10])''' #KEY Error

'''d={1:'RAMESH',2:'SURESH',3:'MAHESh'}
if 400 in d:
    print(d[400])
else:
    print("NOT FOUND.")    

d={1:'Ramesh', 2:'Suresh', 3:'Mahesh'}
print("Before deleting key from dictionary", d)
del d[1]
print("After deleting key from dictionary:",d)'''

#Functions and methods of Dictionary
#1
'''d=dict()
print(d)
#2
d=dict(1:'Ramesh',2:'Suresh',3:'Mahesh')
print(d)'''

#POP()
'''d={1:'Ramesh',2:'Suresh',3:'Mahesh'}
print("before pop:",d)
d.pop(1)
print("after pop:",d)'''

#popitem()
'''d={}
d.popitem()
print("After popitem:",d)'''

#items():-gives you a tupple with values and key
'''d={1:'Ramesh',2:'Suresh',3:'Mahesh'}
for k,v in d.items():
    print(k,"---",v)'''

#Comprehension
'''l1=[1,2,3,4,5,6,7,8]
d={i:i**2 for i in l1}
l2=[i**2 for i in l1]
t=(i**2 for i in l1)
print(l2)
print(d)
print(t)'''




