#Single Inheritance in Classes

class Parent: #parent class or base class
    parentname=""
    sonname = ""
    daughtername = ""

    def show(self):
        print(self.parentname)

class Child(Parent): #childclass or derived class
    childname=""
    def display(self):
        print(self.childname)

c=Child() #object of child class
c.parentname="john"
c.childname="arthur"
c.show() # parent class method
c.display() #child class method


#Multiple Inheritance

class Son(Parent):
    def display(self):
        print(self.sonname)

class Daughter(Parent):

    def print_d(self):
        print(self.daughtername)

s=Son()
s.sonname="William"
d=Daughter()
d.daughtername="Alice"
d.parentname="John"
d.show()
d.print_d()
s.display()

#multiple Parent Class Inheritance
class Father:
    fathername=""
class Mother:
    mothername=""

class Child(Father,Mother):
    def __init__(self,childname):
        self.childname=childname
c=Child("Arthur")
c.fathername="John"
c.mothername="Alisa"
print(c.childname,c.fathername,c.mothername)
