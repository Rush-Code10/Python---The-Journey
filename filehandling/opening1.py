fhand = open('buh.txt')

print(fhand,'\n')
count = 0

#TO SEE THE NUMBER OF CHARACTERS
inp = fhand.read()
print("Length:",len(inp))
print(inp[:12],"\n")

#TO COUNT NUMBER OF LINES
for i in inp:
    if(i == '\n'):
        count = count + 1
print("Number of lines:",count+1)

'''
for i in inp:
    count = count + 1
    print(i)
print('Line Count:',count)
'''