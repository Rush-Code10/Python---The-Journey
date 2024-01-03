import re

# Matching all the numbers in the sentence that contain digits betwen
x = 'I have 10 favourite Manga on the bookshelf 20 , 7 , 4 and 3 respectively'
y = re.findall('[0-9]+',x)
print(y)

a = 'Rushabh Is The Best'
b = re.findall('[AEIOU]+',a)
print(b)

# Greedy Matching
email = 'From: Use : character '
fy = re.findall('^F.+:',email)
print(fy)
fyy = re.findall('^F.+?:',email)
print(fyy)