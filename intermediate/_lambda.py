# Lambda function generally makes a function a one liner .. simple enough

twice = lambda num : num * 2
#OTHERWISE  WULD HAVE TO WRITE IT AS
'''
def twice(num):
    return num*2
'''
multiply = lambda a,b : a*b
#OTHERWISE  WULD HAVE TO WRITE IT AS
'''
def multiply(a,b):
    return a*b
'''
print(multiply(2,6))
print(twice(19))