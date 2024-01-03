def addtwo(a,b):
    added = a + b
    return added

def subtwo(a,b):
    subbed = a - b
    return subbed

def multiplytwo(a,b):
    multiplied = a * b
    return multiplied

def dividetwo(a,b):
    divided = a / b
    return divided

symbol = input('''ENTER A SYMBOL( + - * / ): ''')
num1 = float(input("ENTER NO.1: "))
num2 = float(input("ENTER NO.2: "))

if(symbol == '+'):
    print(addtwo(num1,num2))
elif(symbol == '-'):
    print(subtwo(num1,num2))
elif(symbol == '*'):
    print(multiplytwo(num1,num2))
elif(symbol == '/'):
    print(dividetwo(num1,num2))
else:
    print("INVALID INPUT")