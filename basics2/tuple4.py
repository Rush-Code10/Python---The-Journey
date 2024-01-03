# sort values by key
d = {'a':10,'d':25,'b':9,'c':5}
tmp = list()
for k,v in d.items():
    tmp.append((v,k))
print("Tuple with sub list :", tmp)
t = sorted(tmp,reverse=True)
print("Tuple with sub list but SORTED:",t)