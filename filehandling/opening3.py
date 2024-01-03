fname = input("ENTER FILE NAME: ")
try:
    fhand = open(fname)
except:
    print("FILE CANNOT BE OPENED: ",fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('B'):
        count = count + 1
print("There are",count,"lines in",fname,"that start with 'B'")