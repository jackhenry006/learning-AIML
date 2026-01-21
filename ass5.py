# class question
"""
data=True
line=1
with open("sample.txt","r") as f:
    
    while data:
        data=f.readline()
        if("python" in data):
            print(f"Word Found at line number : {line}")
            break

        line+=1
"""

# q1
"""
with open("sample.txt","w") as f: 
    f.write("ankit\nsunil\nabhishek\nswastik\nblesson")

with open("sample.txt","r") as f:
    data=f.read()
    print(data)
"""

#q2

"""
with open("sample.txt","a+")as f:
    num=int(input("Enter the number of logs you want to enter : "))
    for i in range(num):
        data=input("Enter the log : ")
        f.write(data)

with open("sample.txt","r") as f:
    value=f.read()
    print(value)

"""