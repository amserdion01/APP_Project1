from asyncio.windows_events import NULL
from distutils.log import error
from category import Category
from categories import Categories
from json import JSONDecodeError
from product import *
from products import *

def add_to_cart():
    ex = "n"
    while(ex == "n"):
        print("1.List all the products \n2.List all the products from a certain category 3.Exit\n")
        op = int(input("Enter an option between 1 and 3: "))  
        match op:
            case 1:
                Products.load_products_all()
                prod =      
            case 2:   
                t = int(input("Possible category of producs:\n1:Amplifier\t2:Reciever\t3:Turntable\nEnter the number of the wanted category: "))
                products= Products.load_products(t)
                for prod in products:
                    for key, value  in prod.__dict__.items():
                        print(f"{key}:{value}, ")
                    print("\n")
            case 3:
                t = int(input("Possible category of producs:\n1:Amplifier\t2:Reciever\t3:Turntable\nEnter the number of the wanted category: "))
                Products.add_product(t)
            case 4:
                t = int(input("Possible category of producs:\n1:Amplifier\t2:Reciever\t3:Turntable\nEnter the number of the wanted category: "))
                Products.remove_product(t) 
            case 5:
                print("Have a nice day!")
                exit()
            case _:
                error_handler()
        ex = input("Do you want to exit the category menu? (y/n): ")      