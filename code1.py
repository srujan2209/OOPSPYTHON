# Instance Attributes and constructor
# Instance attribute of a particluar class is used as constructor

# In python we use init constructor(methos) to define the instance attibutes of a particular class.
class Tedddy:
    # KEY POINTS:
    # Quantity is the class attributes
    qunatity = 200

    # Instance attributes,
    # self is nothinf but reference to the current instance.
    # __init__ is a constructor
    def __init__(self,name,color):   # here name and color are two attributes of a particluar class
        self.name = name
        self.color = color

# Object
teddy1 = Tedddy('Tedd','RED')
print(teddy1.name)
print(teddy1.color)
print(teddy1.qunatity)

teddy2 = Tedddy('Rob','Brown')
print(teddy2.name)
print(teddy2.color)
print(teddy2.qunatity)

