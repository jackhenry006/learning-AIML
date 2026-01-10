#Q1

"""
value = input("Enter the string: ")

plain=value[::-1]

if(plain==value):
    print("It is a plaindrome")
else:
    print("It is not a plaindrome")

#Another Method

rev=""
for str in value:
    rev=str+rev

if(rev==value):
    print("It is a plaindrome")
else:
    print("It is not a plaindrome")

"""
#Q2

"""
num = [1,2,3,4,5]

total= len(num)
sum=0
for i in num:
    sum=i+sum

print(f"The Average of the values is : {sum/total} ")

"""

# Q3

"""
n=int(input("Enter the number of elements you want to enter in the 1st list: "))
list1 = []
for i in range(n):
    value=int(input("Enter the values "))
    list1.append(value)
    
n1=int(input("Enter the number of elements you want to enter in the 2nd list: "))
list2=[]
for i in range(n1):
    value1=int(input("Enter the values "))
    list2.append(value1)

result=list1+list2
result.sort()

print(result)

"""
#Q4

"""
tup=(1,2,3,4,5,6,7,8,9)
tup1=list(tup)      #Type conversion kora hela 


even=[]
odd=[]

for num in tup1:
    if(num%2==0):
        even.append(num)
    else:
        odd.append(num)

a=tuple(even)
b=tuple(odd)

print(f"The EVEN numbers are : {a}")
print(f"The ODD numbers are : {b}")

"""

# Q5

"""
stu_profile={}


print("Enter the operation according to your need")
print("A for adding a student")
print("B for updating marks")
print("C for searching for a student")
print("D for displaying all students and marks")

operation=input("Enter the type of operation you want to perform in the student profile: ").upper()

if(operation=="A"):
    name=input("Enter the name : ")
    marks=int(input("Enter the marks: "))
    stu_profile[name]=marks
    print("Student added sucessfully")
elif(operation=="B"):
    name = input("Enter the name: ")
    if(stu_profile==name):
        marks=int(input("Enter the new marks: "))
        stu_profile[name]=marks
        print("Your mark is updated")
    else:
        print("Enter the valid name")
elif(operation=="C"):
    name=input("Enter the name: ")
    if(stu_profile==name):
        print("The student is present in the dict")
    else:
        print("The student is not present in the dict")
elif(operation=="D"):
    print(stu_profile.items())
else:
    print("Enter a valid operation")
"""

#Q6

"""
words = ["apple", "banana", "kiwi", "cherry", "mango"]

dictionary={}

for str in words:
    value=len(str)
    dictionary[str]=value
print(dictionary)
"""

# Q7

"""
value = input("Enter a sentence to know how many spaces are present in that sentence: ")
total=0

i=0
while i<len(value):
    if(value[i]==" "):
        total += 1
    i+=1
print(total)
"""

# Q8
"""

list1 = [1, 2, 3, 4] 
list2 = [5, 6, 7, 8]
l1=set(list1)
l2=set(list2)

if(l1.intersection(l2)!=0):
    print("There is a  no common element in this two list")
else:
    print(f"There is a common element in this two list")

"""

# Q9

"""
list1 = [1, 2, 3] 
list2 = [3, 4]
l1=set(list1)
l2=set(list2)
print(l1.intersection(l2))

"""

#Q10

"""
value=input("Enter the string: ")
val=set(value)
val1=set(value)
result=val.intersection(val1)
    
print(result)
print(len(result))
"""

