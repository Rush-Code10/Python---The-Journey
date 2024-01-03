l = list()
t = tuple()
d = dict()
print(f"List functions are : {dir(l)}")
print(f"Tuple functions are : {dir(t)}")
print(f"Dictionary functions are : {dir(d)}")

# How to update a value in a dictionary
d1 = {"A":"Raisin",'B':'Cashews','C':'Almonds'}
print(d1)
d1.update(C = 'Pista')
print(d1)