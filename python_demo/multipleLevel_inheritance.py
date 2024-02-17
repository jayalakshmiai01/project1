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
#sub class
class child(parent):
    def __init__(self):
        
        super().__init__()
        super().AadharAccess()
        super().classRoom()
        super().lab1()
        super().lab2()
        super().aibatch()
        super().cadbatch()
        print("\nchild class is AIBATCH")
       
    def student(self):
        print("i am a student")
class visitors(child):
    pass
#object********************************************************
# s=child()

# s.car()
v=visitors()
v.student()