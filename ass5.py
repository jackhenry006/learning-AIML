# class question
data=True
line=1
with open("sample.txt","r") as f:
    
    while data:
        data=f.readline()
        if("python" in data):
            print(f"Word Found at line number : {line}")
            break

        line+=1


    