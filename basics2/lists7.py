numlist = list()
while True:
    inp = input("Enter Number: ")
    if inp.lower() == 'done':
        print("NUMBERS HAVE BEEN CAUGHT AND TRACED")
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/len(numlist)
print("AVERAGE: ", average)