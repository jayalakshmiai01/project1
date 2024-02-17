class parent():
    def __init__(self):
        print("family name is bright services")
        
    def AadharAccess(self):
        print("need AadharAccess")
    def classRoom(self):
        print("you can access calss room")
    def lab1(self):
        print("you can access lab1")
    def lab2(self):
        print("you can access lab2")
    def aibatch(self):
        print("you can  join  aibatch course")
    def cadbatch(self):
        print("you can join cadbatch course")
class aibatch():
    def __init_(self):
        print("welcome to aibatch")
    def c(self):
        print("i study c")
    def cpp(self):
        print("i study cpp")
    def python(self):
        print("i study python")
class cadbatch(parent,aibatch):
    def __init__(self):
        print("welcome to cadbatch")
        super().__init__()
        super().AadharAccess()
        super().classRoom()
        super().lab1()
        super().lab2()
        super().aibatch()
        super().cadbatch()
        super().c()
        super().cpp()
        super().python()
        

cad=cadbatch()
       