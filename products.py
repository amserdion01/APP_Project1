from json import *
import json
from product import *

class Products():
    
    @classmethod
    def Checktype(self, prod):
        if isinstance(prod,Amplifier):
            return("amplifiers.txt")
        if isinstance(prod,Receiver):
            return("receiver.txt")
        if isinstance(prod,Turntable):
            return("turntable.txt")
        
    @classmethod
    def load_products(self,no):
        if no == 1:
            temp = Amplifier("test",99,99,99)
            file = "try.txt"
        elif no == 2:
            temp = Receiver(99,"red",99)
            file = "receiver.txt"
        elif no == 3:
            temp = Turntable(99,True, 99)
            file = "turntable.txt"
            
        with open(file) as f:
            products = []
            for line in f:
                data = json(loads(line))
                temp = eval(Amplifier(data["name"],data["power"], data["chanel"], data["size"]))
                products.append(temp)
            print(products)
if __name__ == "__main__":
    cat = Products()