#super class
class parent():
    def __init__(self):
        print("family name is bright services")
        
    def welcome(self):
        print("welcome to parent")
    def land(self):
        print("i have 2 lands")
#sub class
class child(parent):
    def __init__(self):
        super().__init__()
        super().welcome()
        super().land()
        print("child class is AIBATCH")
       
    def car(self):
        print("she has a BMW")
#object********************************************************
s=child()

s.car()