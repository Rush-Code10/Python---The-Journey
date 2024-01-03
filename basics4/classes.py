class Dog:
    # THIS IS A CONSTRUCTOR
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print("WOOF!!!")

roger = Dog("Roga",8)
print(roger.name)
print(roger.age)
roger.bark()
print(type(roger))