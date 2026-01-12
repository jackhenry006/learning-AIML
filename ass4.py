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