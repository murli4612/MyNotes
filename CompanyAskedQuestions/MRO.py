class A:
    def __init__(self):
        print("inntialize class A")
    def greet(self):
        print("Class A greet")

class B(A):
    def __init__(self):
        super().__init__()
        print("intialize class B")
    def greet(self):
        print("Class B greet")
class C(A):
    def __init__(self):
        super().__init__()
        print("inialitize C")
    def greet(self):
        print("Class C greet")
class D(B,C):
    def __init__(self):
        super().__init__()
        print("inialitze d")
    def greet(self):
        print("Class D greet")

d_instance = D()
d_instance.greet()