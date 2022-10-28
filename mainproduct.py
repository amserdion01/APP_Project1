from product import *
from products import *
import json

if __name__ == "__main__":
    a = Amplifier("hi",300, 5, 40)
    print(isinstance(a,Amplifier))
    
    Products.load_products(1)