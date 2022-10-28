from json import JSONEncoder, JSONDecoder, dump, loads

# define the Encoder class used in serialization
class Encoder(JSONEncoder):
    def default(self, o: object) -> object:
        return o.__dict__

class Decoder(JSONDecoder):
    """ We have to transform the serialized string into Python objects"""
    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        prod = Product(*vals)
        return prod

# define the Product class, which is the base class for all the  products in the store    
class Product():
    def __init__(self, name):
        self.name = name
    
class Amplifier(Product):
    def __init__(self, name,power, chanel, size ):
        super().__init__(name)
        self.power = power
        self.chanel = chanel
        self.size = size
        
class Receiver(Product):
    def __init__(self, name, chanel, color, size):
        super().__init__(name)
        self.chanel = chanel
        self.color = color
        self.size = size

class Turntable(Product):
    def __init__(self,name, speed, bluetooth, size):
        super().__init__(name)
        self.speed = speed
        self.bluetooth = bluetooth
        self.size = size
    