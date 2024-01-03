# so there is try and excpet
#basically try and except are for error handling like try this and if it doesn't work use that

# string to int/float/double
a = '1.4098'
b = float(a)
print(b)

x = '1.4098sdghf'
try:
    y = float(x)
    print(y)
except:
    print(1.40)