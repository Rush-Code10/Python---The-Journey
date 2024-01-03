# LARGEST AND SMALLEST

option = int(input('''ENTER
1. LARGEST NUMBER
2. SMALLEST NUMBER 
3. ADDITION
4. SUBTRACTION
'''))

nums = input("ENTER NO.S (give spacing between 2 numbers): ")
num_list1 = nums.split() #SPLITS THE ABOVE STRING INTO VARIOUS DIFFERENT SEGMENTS USING THE SPACEBAR
print(num_list1)
num_final = list(map(int, num_list1)) # CONVERTS THE WHOLE STRING LIST INTO INT LIST
print(num_final)
print(" ")

#LARGEST NUMBER
largest_number = num_final[0]
if option == 1:
    for i in num_final:
        if i >= largest_number:
            largest_number = i
    print(f"LARGEST NUMBER: {largest_number}")

#SMALLEST NUMBER
smallest_number = num_final[0]
if option == 2:
    for i in num_final:
        if i <= smallest_number:
            smallest_number = i
    print(f"SMALLEST NUMBER: {smallest_number}")

#ADDITION
add = 0
if option == 3:
    for i in num_final:
        add = i + add
    print(f"ADDITION: {add}")

#SUBTRACTION
sub = 0
if option == 4:
    for i in num_final:
        sub = i - sub
    print(f"SUBTRACTION: {sub}")