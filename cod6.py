# multi-level inheritance
class A:
    def a_method(self):
        print("This is a method")
class B(A):
    def b_method(self):
        print("this is a b method")
class C(B):
    def c_method(self):
        print("this is a c method")

c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()