numbers = [1,2,3,4,5]
number_pow = [n**2 for n in numbers]
print(number_pow)

"""
also can be written by lambda as
number_pow = list(map(lambda n : n**2,numbers))
"""