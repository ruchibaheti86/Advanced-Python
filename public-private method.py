#
class Employee:
    __name="" #private variable

    def __init__(self,name): # constructor
        self.__name=name # initialising the varaible

    def show(self):
        print(self.__name)

    def __changeName(self,name): #private method
        self.__name=name
        return self.__name

    def display(self): #public method
        result=self.__changeName("dggjhk")
        return result


name=input("Enter the name")
e=Employee(name)
#print(e.__changeName("gdsfg"))
print(e.display())