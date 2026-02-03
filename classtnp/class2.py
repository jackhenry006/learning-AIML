"""def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a//b

def mul(a,b):
    return a*b

while True:
    n=input("Enter the function you want to do Add ,sub,div,mul,exit: ").upper()

    if n != "EXIT":
        a=int(input("enter the 1st value: "))
        b=int(input("enter the 2nd value: "))

    if n=="ADD":
       print(add(a,b)) 
    elif n=="SUB":
        print(sub(a,b))
    elif n=="DIV":
        print(div(a,b))
    elif n=="MUL":
        print(mul(a,b))
    elif n=="EXIT":
        break


def vo(n):
    count=0
    for i in n:
        if(i == "aaeiou,AEIOU"):
            count +=1
    print(f"It has {count}")

def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(f"Swapped values are : {a},{b}")
# swap(2,3)

def fib(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fib(25))

def sc(n):
    sq=n**2
    cu=n**3
    print(f"square: {sq} and cube: {cu}")

sc(2)"""

def rev(n):
    
    rev=0
    while n>0:
        z=n%10
        rev=rev*10+z
        n=n//10
    print(rev)
rev(123)