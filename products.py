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
    def remove_product(self, no, name):
        products = self.load_products(no)
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
    def add_to_cart(self, no):
        products = self.load_products(no)
        print("Below you can see the list of products requested:\n")
        for prod in products:
            print(prod.__dict__)
        name = input("What is the name of the object you want to add to cart?\n")
        for product in products:
            if product.name == name:
                print(f"The product: {product.__dict__} is now in your cart")
                p = product.__dict__
                break
        e = Encoder()
        with open("cart.txt", 'a') as f:
            dump(p, f)
            f.write('\n')   
    @classmethod                        
    def make_order(self):
        cart = self.load_cart()
        with open('cart.txt', 'w') as f:
            pass 
        amplifiers = self.load_products(1)
        for am in amplifiers:
            for item in cart:
                if am.__dict__ == item:
                    self.remove_product(1, am.name)
        
        recievers = self.load_products(2)
        for rec in recievers:
            for item in cart:
                if rec.__dict__ == item:
                    self.remove_product(2, rec.name)
        turntables = self.load_products(3)
        for turn in turntables:
            for item in cart:
                if turn.__dict__ == item:
                    self.remove_product(3, turn.name)
        print("Your order has been made")
        
    @classmethod            
    def remove_from_cart(self):
        cart = self.load_cart()
        for product in cart:
            print(product)
        name = input("What is the name of the object you want to remove from cart?\n")
        for product in cart:
            if name == product["name"]:
                print(f"The product: {product} is now removed from your cart")
                cart.remove(product)
                break
        with open("cart.txt", 'w') as f:
            for prod in cart:
                dump(prod, f)
                f.write('\n')            
    @classmethod
    def load_cart(self):
        with open("cart.txt", 'r') as f:
            cart = []
            for line in f:
                line.strip()
                line = json.loads(line)
                cart.append(line)
        return cart     
    
if __name__ == "__main__":
    cat = Products()
    