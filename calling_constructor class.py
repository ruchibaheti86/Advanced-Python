class Father:
    def __init__(self,name):
        print("Welcome",name)

class Mother:
    def __init__(self,n):
        print("Hello",n)

class Child(Father,Mother):
    def __init__(self):
        #super().__init__() #calling parent class constructor
        Father.__init__(self,"John")
        Mother.__init__(self,"Alice")
        print("hi")

c=Child()