fhand  = open('ro.txt')
counts = dict()
for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1

t = sorted([(v,k) for k,v in counts.items()])
t = sorted(t,reverse=True)
for k,v in t:
    print(k,v)

print(t)