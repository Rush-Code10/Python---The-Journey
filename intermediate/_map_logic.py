numbers = [1,2,3,4,5]
'''
def squaring(a):
    return a**2
'''
# THE ABOVE FUNCTION CAN ALSO BE WRITTEN AS :
squaring = lambda a : a**2
#The statement below uses the function squaring and applies it on every value of numbers
result = map(squaring,numbers)
print(list(result))

#AN EVEN MORE SIMPLIFIED VERSION IS WRITTEN IN : _map_advance