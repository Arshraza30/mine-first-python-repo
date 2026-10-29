#Pythonfunc
#Defaultfunc
#Keyword Argument
#Recursive
#Lambda Func
#Func Docstrings

#PYHTON FUNCTION

'''def abcd():
    print("FF")
abcd()

def addnum(a,b):
    print(f"sum is {a+b:.2f}")
addnum(10,20)
addnum(30.9,40.8)'''

#return func
'''def sum(a,b):
    c=a+b
    return c

x=sum(1,2)
print(x)

def m1():
    print("this function is returning nothing")
#function callling
m1()
x=m1()
print(x)'''

'''def m1(a,b):
    c=a+b
    d=a-b
    return c,d
x,y=m1(10,5)
print("sum:",x)
print("sub:",y)'''

'''def add():  #func aliasing
    print("we assigned function to variable")
sum=add
sum()    

def message(text):
    print(text)
def printmessage(x):
    x("hello world")
printmessage(message)''' 

#Recursive function
'''Suppose a func needs to be called 10 times, recursive func says the func will be called once and it will call itself the other 9 times'''
'''it is nothing but if and else
where if is the stopping condition and 
else stands for recalling it'''

'''def sumofdigits(number): #works on string
    if number=="":
        return 0
    else:
        return int(number[0])+sumofdigits(number[1:])
print(sumofdigits("12345"))


def sod(num):      #works on number
    if num==0:
        return 0
    else:
        return (num%10)+sod(num//10)
print(sod(12345))


def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
print(power(2,3))'''   

'''def sod(num,s):
    if num==0:
        return s
    else:
        return sod(num//10,s+(num//10))
print(sod(1234,0))    

def strrev(str,rev):
    if str=="":
        return rev
    else:
        return strrev(str[:-1],rev+str[-1])
print(strrev("yes",""))'''

def pal(str,end,start):
    if start==end:
        return True
    elif str[start]!=str[-(start+1)]:
        return False
    else:
        return pal(str,end,start+1)
print(pal("RAJ",len("RAJ"),0))    

    
    
    






