class Animal:
    def walk(self):
        print("Walking....")
#Dog class inherits animal class
class Dog(Animal):
    # THIS IS A CONSTRUCTOR
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print("WOOF!!!")

roger = Dog("Roga",8)
roger.walk()