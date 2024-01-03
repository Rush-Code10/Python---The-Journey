import re
s = input("Enter String: ")
num = input("Enter Number: ")
pattern = f'^{num}'

if re.search(pattern,  s):
  print('Found a match!')
else:
  print('Not matched!')