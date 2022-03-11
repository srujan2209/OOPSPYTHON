# Implementing Methods in Object oriented.
class Teddy:
    quantity = 200

    def __init__(self,name,color):
        self.name = name
        self.color = color

    # This is the Method to change the color of a teddy bear
    def change_color(self,color):
        print("This is a method")
        self.color = color

# this is a object
teddy1 = Teddy('Ted','Red')
print(teddy1.name)
print(teddy1.color)

teddy1.change_color("Blue")
print(teddy1.name)
print(teddy1.color)

