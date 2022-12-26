from itertools import product
from json import *
import json
from json import decoder
from product import *
import category

def convert_int(n):
    try:
        return int(n)
    except ValueError:
        return n
    
class Products():
    
    @classmethod
    def checktype(self, no):
        if no == 1:
            file = "amplifier.txt"
        elif no == 2:
            file = "receiver.txt"
        elif no == 3:
            file = "turntable.txt"
        return file
    
    @classmethod
    def add_product(self, no):
        products = self.load_products(no)        
        types = products[0].__dict__.keys()
        temp = {}
        for t in types:
            temp[t] = convert_int(input(f"Enter the {t} of the product:"))
        with open(self.checktype(no), 'a') as f:
            prod = json.dumps(temp)
            dump(prod, f)
            f.write('\n')

                
            
    @classmethod
    def load_products(self,no):
        with open(self.checktype(no)) as f:
            products = []
            for line in f:
                data = loads(line)
                data = json.loads(data)
                print(data)
                if no == 1:
                    temp = Amplifier(**data)
                elif no == 2:
                    temp = Receiver(**data)
                elif no == 3:
                    temp = Turntable(**data)
                products.append(temp)
        return products
    
    @classmethod
    def load_products_all(self):
        print("Receivers:")
        with open("receiver.txt") as f:
            for line in f:
                data = loads(line)
                data = json.loads(data)
                print(data)
        print("\nAmplifiers:")
        with open("amplifier.txt") as f:
            for line in f:
                data = loads(line)
                data = json.loads(data)
                print(data)
        print("\nTurntables:")
        with open("turntable.txt") as f:
            for line in f:
                data = loads(line)
                data = json.loads(data)
                print(data)
        
    @classmethod
    def remove_product(self, no):
        
        products = self.load_products(no)
        print("Below you can see the list of products requested:\n")
        for prod in products:
            print(prod.__dict__["name"])
            
        name = input("What is the name of the object you want to delete?\n")
        for product in products:
            if product.name == name:
                print(f"The object: {product.__dict__} will be deleted")
                products.remove(product)
                break
        e = Encoder()
        
        with open(self.checktype(no), 'w') as f:
            for prod in products:
                prod = json.dumps(prod.__dict__)
                dump(prod, f)
                f.write('\n')
    @classmethod
    def cart(self, no):
        
        products = self.load_products(no)
        print("Below you can see the list of products requested:\n")
        for prod in products:
            print(prod.__dict__["name"])
            
        name = input("What is the name of the object you want to add to cart?\n")
        for product in products:
            if product.name == name:
                print(f"The object: {product.__dict__} will be deleted")
                p = product.__dict__
                break
        e = Encoder()
        print(p)
        with open("cart.txt", 'a') as f:
            dump(p, f)
            f.write('\n')   
            
    def make_order(self):
        with open("cart.txt", 'w') as f:
            products = []
            for line in f:
                products.append(line)
        amplifiers = self.load_products("amplifier.txt")
        recievers = self.load_products("receiver.txt")
        turntables = self.load_products("turntable.txt")
        print(amplifiers)

            
if __name__ == "__main__":
    cat = Products()
    cat.make_order()
    
    