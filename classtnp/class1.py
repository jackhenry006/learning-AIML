n=int(input("enter the number: "))

if(n<0):
    print("You etered the number is negative")
elif(n>0):
    print("your entered number is positive")
else:
    print("your enterd number is equal to 0")

if(n%2==0):
    print("the number is even")
else:
    print("The number is odd")

for i in range(1,11):
    print(i)

for i in range(1,11):
    print(f"The table is: {i*n}")

i=10
while i>0 :
    print(i)
    i -=1

i=1
sum=0
while i<=100:
    sum=sum+i
    i+=1

a=int(input("Enter the number"))
b=int(input("enter  the number"))

add=a+b
sub=a-b
div=a//b
mul=a*b

print(add,sub,div,mul)

x=0
y=True
z=4.5
print(type(x))
print(type(y))
print(type(z))

for i in range(1,10):
    if i>5:
        print(i)
        break

for i in range(1,11):
    if(i%2==0):
        continue
    print(i)

def cal(a,b):
    add=a+b
    dif=a-b
    print(add,dif)

hii=int(input("Enter any number between 1-5 to see a message"))
match hii:
    case 1: print("hii")
    case 2: print("hii")
    case 3: print("hii")
    case 4: print("hlo")
    case 5: print("hii")

n=int(input("enter the number of rows: "))

for i in range(0,n+1):
    for j in range(i):
        print("*" ,end=" ")
    print()