#index
'''a="This is a merged batch, we will complete string today."
print(id(a))
b=a.count("a")
print(b)
print(id(a))'''

'''a="This is a merged batch, we will complete string today."
print(id(a))
b=a.count("pyhton")
print(b)
print(id(a))'''

'''a="This is a merged batch, we will complete string today."
print(id(a))
print(a)
c=a.replace("today", "tomorrow")
print(c)
print(id(c))
b=a.count("a")
b=c.count("a")
print(b)
print(id(a))'''

'''a="Python programming language."
n=a.split()
print("Before splitting:", a)
print("After Splitting", n)
print(type(n))
for x in n:
    print(x)

a="Python programming language, Python is easy."
n=a.split()
print("Before splitting:", a)
print("After Splitting", n)
print(type(n))
for x in n:
    print(x)    '''

'''a="13:32:55"
h,m,s=a.split(":")[0],a.split(":")[1],a.split(":")[2]
print(h)
print(m)
print(s)'''

'''a="13:32:55"
n=a.split(":")
print(n)
for x in n:
    print(x)'''

'''l1=["Rohan", "Rahul", "Chetan", "Rajesh", "Rakesh"]
a="-".join(l1)
print(a)'''

'''a=['Roshan', 'actor', 'India']
candidate="-".join(a)
print(candidate)'''

'''name="raj"
s=input("Enter fixed name: ")
if name==s.lower()
    print("OK")
else:
    print("NOT OK")''' 

'''name="MUTTU Swami CHin swami VENdu GOPAL IYYar"
print(name.lower())
print(name.upper())
print(name.swapcase())
print(name.title())
print(name.capitalize())
print(name.isalnum())
val=input("Enter value")
val= val if val.isalpha() else eval(val)
print(val)
print(type(val))'''


#string interpolation
'''name="Rohit"
age="18"
places="Delhi"
sub="{b} lives in {c} and his age is {a}".format(a=age,b=name,c=places)
print(sub)

name="Rohit"
age="18"
place="Delhi"
sub=f"{name} lives in {place} and his age is {age}"
print(sub)'''

'''a=input("Enter a string: ")
b=""
n=a.split(" ")
for x in n:
    even=x[::2]
    b+=even+" "
print(b.strip())'''

'''a=input("Enter a string: ")
b=a.count()'''