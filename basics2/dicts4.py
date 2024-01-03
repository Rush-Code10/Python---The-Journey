counts = dict()
names = ['rush','wesh','uish','wesh','lack','rush','rush','lack']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)