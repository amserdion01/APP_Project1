from product import *
from products import *
import json


def add():
    print("Which type of product do you want to add?\n")
    t = int(input("Possible category of producs:\n1:Amplifier\t2:Reciever\t3:Turntable\n"))
    Products.add_product(t)

if __name__ == "__main__":
    a = Amplifier("hi",300, 5, 40)
    
    
    add()