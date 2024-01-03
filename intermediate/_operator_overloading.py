class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __gt__(self,other):
        return True if self.age>other.age else False
roger = person('ROGER',50)
whitey = person('WHITEBEARD',56)

print(roger<whitey)