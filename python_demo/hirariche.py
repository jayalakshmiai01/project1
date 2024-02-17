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
class aibatch(parent):
    def __init__(self):
        super().__init__()
        super().AadharAccess()
        super().classRoom()
        super().lab1()
        super().lab2()
        super().aibatch()
        super().cadbatch()
        print("\nwelcome to AIBATCH")
       
    def c(self):
        print("i study c")
    def cpp(self):
        print("i study cpp")
    def python(self):
        print("i study python")
class cadbatch(parent):
    def __init__(self):
        super().__init__()
        super().AadharAccess()
        super().classRoom()
        super().lab1()
        super().lab2()
        super().aibatch()
        super().cadbatch()
        print("\nchild class is CADBATCH")
    def javascript(self):
        print("i study javascript")
    def csharp(self):
        print("i study csharp")
    def htmCss(self):
        print("i study htmlCss")

ai=aibatch()
cad=cadbatch()