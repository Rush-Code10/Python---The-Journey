numbers = [1,2,3,4,5,6,7,8,9,10]

def isEven(n):
    return n%2 == 0

# Will store isEven values means it will filter it
result = filter(isEven , numbers)
print(list(result))

#Simplified code is written in _filter_advance