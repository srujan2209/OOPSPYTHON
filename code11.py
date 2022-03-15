"""Encapsulation or DataHiding in python"""
# Uses : # Hiding or protecting Data from external users
# For Hiding the variable we can use __ at the start of the varibalename

class Myclass:
    __hiddenvariable = 0
    def add(self,other):
        self.__hiddenvariable+=other
        print(self.__hiddenvariable)

objectone = Myclass()
objectone.add(25)
print(objectone)

