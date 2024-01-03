# Sorting lists of tuples

d = {'a':10,'d':25,'b':9,'c':5}
print(d.items())
print(sorted(d.items()))
t = sorted(d.items())
print("UNSORTED")
for k,v in d.items():
    print(k, v)
print("SORTED")
for k,v in t:
    print(k, v)