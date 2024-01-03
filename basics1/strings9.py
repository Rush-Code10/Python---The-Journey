data = "From rushabh.shah@gmail.com SAT JAN 5 09:14:16 2008"
pos1 = data.find(' ')
print(pos1)
pos2 = data.find('@')
print(pos2)
pos3 = data.find(' ',pos2)
print(pos3)

print(f"EMAIL ID: {data[pos1+1 : pos3]}")