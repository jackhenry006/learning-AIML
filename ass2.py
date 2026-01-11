#Q1
"""

salary=int(input("Enter the salary to know the final tax rate: "))

if(salary<=30000):
    print(f"The final tax rate is 5% for the salary of {salary}")
elif(salary>30000 and salary<=70000):
    print(f"The final tax rate is 15% for the salary of {salary}")
elif(salary>70000):
    print(f"The final tax rate is 25% for the salary of {salary}")

"""

#Q2

"""

def evod(a,b):
    for i in range(a,b):
        if(i%2==0):
            print(f"The even number is : {i}")
        else:
            print(f"The odd numer is: {i}")

a=int(input("Enter the number from where you want to start: "))
b=int(input("Enter the number you want to end: "))

print(evod(a,b))

"""

# Q3
"""

def digit(n):
    N=0
    i=0
    while i<=n:
        N=n%10
        n=n//10
        print(N)
        i+=1
    
digit(312)

"""

# Q4

"""

def count(n):
    N=0
    digit=0
    i=0
    while i<n:
        N=n%10
        digit +=1
        n=n//10
        i+=1
    digit+=1
    print(f"The number of digit present in the number is: {digit}")

num=int(input("Enter the Number: "))
count(num)

"""

# Q5

"""

def total(n):
    sum=0
    N=0
    i=0
    while i<n:
        N=n%10
        sum=sum+N
        n=n//10
        i +=1
    print(sum)

num=int(input("Enter the Number: "))
total(num)

"""

# Q6

"""

print("Printing the number which are divisible by both 3 & 5 in between 1 to 100.")

for i in range(1,100):
    if(i%3==0 and i%5==0):
        print(i)

"""

# Q7

"""
while True:
    n=input("Enter the Number to check it is positive or negative and QUIT to stop: ")

    if(n.lower()=="quit"):
        print("The Program is stopped")
        break

    number=int(n)
    if(number>0):
        print(f"The numbewr is positive: {n}")
    elif(number<0):
        print(f"The number is negative: {n}")
    else:
        print("It is zero")
"""

# Q8

"""
def calculator(a,b,operation):

    if(operation=="+"):
        add=a+b
        print(add)
    elif(operation=="-"):
        sub=a-b
        print(sub)
    elif(operation=="*"):
        multi=a*b
        print(multi)
    elif(operation=="/"):
        div=a/b
        print(div)
    else:
        print("Entter a valid operation to perform the calculation")

a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
operation=input("Enter the operation (+,-,*,/) to perform on a & b : ")

calculator(a,b,operation)

"""
# Q9
"""

def is_prime(n):
    
    for i in range(2,n-1):
        if(n%i==0):
            print("The number is prime")
            break
        else:
            print("The number is not prime")
            break

is_prime(8)

"""

#Q10
"""

print("Welcome to number guessing game!!")

print("I will tell you that you gussed the number or not")
number=123

while True:
    num=int(input("Enter the number: "))
    if(number==num):
        print("YOU GUSSED IT CORRECTLY | YOU WON")
        break

    if(num>number):
        print("YOU ARE TOO HIGH!!")
    elif(num<number):
        print("YOU ARE TOO LOW!!")
        
"""
