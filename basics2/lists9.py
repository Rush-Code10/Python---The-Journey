line = 'From rushabh@yahoo.com SAT JAN 2022'
words = line.split()
email = words[1]
emailprovider = email.split('@')
print(emailprovider[1])