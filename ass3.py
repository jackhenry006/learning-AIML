#q1

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