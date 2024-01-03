import re

hand = open('roy.txt')
for line in hand:
    line = line.rstrip()
    if re.search('Blah',line): # FOR STARTSWITH IL ENTER : if re.search('^Blah',line):
        print(line)