# INHERITANCE

class Students:

    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def get_data(self):
        self.name = input("Enter name")
        self.age  = input("Enter age")

    def put_data(self):
        print(self.name)
        print(self.age)

class ScienceStudents(Students):
    def science(self):
        print("This is a science class")

a = ScienceStudents("","")
a.get_data()
