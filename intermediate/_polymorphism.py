"""
Polymorphism is one of the core concepts of object-oriented programming (OOP) and describes situations in which
something occurs in several different forms. In computer science, it describes the concept that you can access
objects of different types through the same interface.
"""
class man:
    def gender(self):
        print("MAN")
class woman:
    def gender(self):
        print("WOMAN")

person1 = man()
person2 = woman()

person1.gender()
person2.gender()