# class question
"""

class product:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        product.count +=1

    def display(self):
        print(f"The Product name is {self.name} and the price is {self.price}")

    @classmethod
    def total(cls):
        print(f"Total Producy in the Store is {cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        print(f"The Discounted Price = {price-(price*discount/ 100)}")
    
    
p1=product("Laptop","50_000")
p2=product("phone","20_000")
p3=product("pen","20")
p1.display()
p2.display()
p3.display()
product.total()
p1.calc_discount(50_000,12)

"""

# Q1
"""
class Bank_Account:
    def __init__(self,account_number,owner_name,balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance

    def deposit(self):
        print(f"Your Amount Has been deposited to the account {self.account_number} , {self.owner_name} , balnce:{self.balance}")

    def withdraw(self):
        print(f"Your Amount Has been deducted from the account {self.account_number} , {self.owner_name} , balnce:{self.balance}")

    def check_balance(self):
        print(f"Your account has balance  {self.account_number} , {self.owner_name} , balnce:{self.balance}")


bank=Bank_Account("12344567","Ankit","50_0000")
bank.deposit()
bank.check_balance()
bank.withdraw()
"""

# Q2

"""
class Book():
    def __init__(self):
        self.title="Harrypotter"
        self.author="author"
        self.review=[]

    def add_review(self,new_review):
        self.review.append(new_review)
        print("Your review is added Sucessfully")

    def count(self):
        print(f"The total reviews are: {len(self.review)}")

    def display(self):
        if not self.review:
            print("Ther is no Review")
        else:
            print(f"The Reviews are : {self.review}")

bk=Book()
yn=input("Do you want to eter a review yes or no: ")

if(yn.upper()=="YES"):
    value=input("Enter the review : ")

bk.add_review(value)
bk.count()
bk.display()
"""

# Q3
"""
class student():
    def __init__(self,name,marks,rollno):
        self.__name=None
        self.__marks=None
        self.__rollno=None

        self.set_name(name)
        self.set_marks(marks)
        self.set_rollno(rollno)
    
    def set_name(self,nam):
        if(nam != ""):
            self.__name=nam
            print("The name is added sucessfully")
        else:
            print("The name space cant be empty")
            
    def set_marks(self,mar):
        if(mar>=0):
            self.__marks=mar
            print("Your mark is updated Sucessfully")
        else:
            print("The mark cant be negative")
            
    
    def set_rollno(self,roll):
        if(1<=roll<=100):
            self.__rollno=roll
            print("Your roll no is updated sucessfully")
        else:
            print("The roll no must be in the between of 1 to 100")

    def get_name(self):
        print(self.__name)

    def get_rollno(self):
        print(self.__rollno)
    
    def get_marks(self):
        print(self.__marks)
    

s1 = student("Ankit",56,34)

s1.get_name()
s1.get_rollno()
s1.get_marks()
"""

# Q4
"""
class shape():
    
    def area(self):
        print("it invokes")

class circle(shape):

    def area(self,radius):
        
        circle_area=3.14*radius**2
        print(f"The radius of the circle is : {circle_area}")

class rectangle(shape):
    def area(self,ln,br):
        rect_area=ln*br
        print(f"The area of the rectangle is: {rect_area}")

class triangle(shape):
    def area(self,ba,he):
        tri_area=0.5*ba*he
        print(f"The area of the triangle is: {tri_area}")
        

c = circle()
r = rectangle()
t = triangle()

c.area(2)
r.area(3,5)
t.area(2,4)
"""

# Q5
"""
class Vechile():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class bike(Vechile):

    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc=engine_cc

    def display_bike(self):
        print(f"The brand of the bike is: {self.brand}")
        print(f"The model of the bike is: {self.model}")
        print(f"The cc of the bike is: {self.engine_cc}")

class car(Vechile):
    def __init__(self,brand,model,seats):
       super().__init__(brand,model)
       self.seats=seats
    

    def display_car(self):
        print(f"The brand of the car is: {self.brand}")
        print(f"The model of the car is: {self.model}")
        print(f"The of seats of the car is: {self.seats}")


bi=bike("hero","od10d342","350cc")
ca=car("lambo","od10d34267",4)

bi.display_bike()
ca.display_car()

"""

# Q6
"""
from abc import ABC , abstractmethod

class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(employee):
    def calculate_salary(self,sal):
        print(f"The salary of an intern : {sal}")

class FullTimeemployee(employee):
    def calculate_salary(self,sal):
        print(f"The salary of an full time employee : {sal}")

class ContractEmploye(employee):
    def calculate_salary(self,sal):
        print(f"The salary of a contract employee : {sal}")

fresher=Intern()
full=FullTimeemployee()
con=ContractEmploye()

fresher.calculate_salary(20_000)
full.calculate_salary(60_000)
con.calculate_salary(90_000)
"""

