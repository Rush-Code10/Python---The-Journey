import re
s = input("Enter String: ")
pattern = '^W(o*)w$|^W(.)w$'
if re.search(pattern,  s):
  print('Found a match!')
else:
  print('Not matched!')