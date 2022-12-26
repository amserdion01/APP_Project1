from asyncio.windows_events import NULL
from distutils.log import error
from category import Category
from categories import Categories
from json import JSONDecodeError
from product import *
from products import *

# define some functions to be used in the main menu. You can follow the
# suggestion described in the lab requirement, by simulating a switch
# instruction using a dictionary, or just using multiple 'if' branches
# which is, obviously, much uglier
def add():
    print("Which type of product do you want to add?\n")
    t = int(input("Possible type of producs:\n1:Amplifier\t2:Reciever\t3:Turntable\n"))
    Products.add_product(t)
    
def add_category(category):
    cat = Category(category)
    Categories.add_category(cat)
    print(f"\nCategory'{category}' added\n")

def delete_category(category):
    cat = Category(category)
    Categories.remove_category(cat)
    print(f"\nCategory'{category}' deleted\n")

def list_categories():
    try:
        print("Below you can see the list of categories:\n")
        categories = Categories.load_categories()
        for cat in categories:
            print(cat.name)
        print("\n")
    except JSONDecodeError as e:
        categories = None

def rmv_product(no):
    products = Products.load_products(no)
    print("Below you can see the list of products requested:\n")
    for prod in products:
        print(prod.__dict__["name"])
    name = input("What is the name of the object you want to delete?\n")
    Products.remove_product(no, name)  
      
def error_handler():
    print("Action not supported\n")
if __name__ == "__main__":
    while True:
        print("1.Category menu \n2.Product menu \n3.Order menu\n4.Exit\n")
        option = int(input("Enter an option between 1 and 4: "))
        match option:
            #category menu
            case 1:
                ex = "n"
                while(ex == "n"):
                    print("1.List all the categories \n2.Add a new category \n3.Delete a category\n4.Exit\n")
                    op = int(input("Enter an option between 1 and 3: "))
                    match op:
                        case 1:
                            list_categories()
                        case 2:
                            category = input("Enter the name of the category you want to add: ")
                            add_category(category)
                            print("This is the new list of categories:\n")
                            list_categories()
                        case 3:
                            category = input("Enter the name of the category you want to delete: ")
                            delete_category(category)
                            print("This is the new list of categories:\n")
                            list_categories()
                        case 4:
                            print("Have a nice day!")
                            exit()
                        case _:
                            error_handler()
                    ex = input("Do you want to exit the category menu? (y/n): ")       
            #product menu
            case 2:
                ex = "n"
                while(ex == "n"):
                    print("1.List all the products \n2.List all the products from a certain category \n3.Add a new product\n4.Delete a product\n5.Exit\n")
                    op = int(input("Enter an option between 1 and 3: "))  
                    match op:
                        case 1:
                            Products.load_products_all()     
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
                            rmv_product(t)
                        case 5:
                            print("Have a nice day!")
                            exit()
                        case _:
                            error_handler()
                    ex = input("Do you want to exit the product menu? (y/n): ")       

            #order menu
            case 3:
                ex = "n"
                while(ex == "n"):
                    print("1.List all the products from the cart \n2.Add a product to the cart  \n3.Remove a product from the cart\n4.Make an order\n5.Exit\n")
                    op = int(input("Enter an option between 1 and 3: "))  
                    match op:
                        case 1:
                            cart = Products.load_cart()
                            print(cart)
                        case 2:
                            t = int(input("Possible category of producs:\n1:Amplifier\t2:Reciever\t3:Turntable\nEnter the number of the wanted category: "))
                            products= Products.load_products(t)
                            i =1
                            Products.add_to_cart(t)
                        case 3:    
                            Products.remove_from_cart()
                        case 4:
                            Products.make_order()
                        case 5:
                                print("Have a nice day!")
                                exit()
                        case _:
                            error_handler()
                    ex = input("Do you want to exit the order menu? (y/n): ")       
            #exit 
            case 4:
                exit()
            case _: 
                error_handler()
                
        