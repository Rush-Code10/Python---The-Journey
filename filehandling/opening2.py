#SEARCHING THROUGH A FILE
#1st Way
'''
fhand = open('buh.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('B'):
        print(line)
'''
#2nd Way
fhand = open('buh.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('B'):
        continue
    print(line)

