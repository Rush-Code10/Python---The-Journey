import re

hand = open('wildcards.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^C.*:',line):
        print(line)

print('\n NEXT \n')

hand = open('wildcards.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X:\S+-',line):
        print(line)