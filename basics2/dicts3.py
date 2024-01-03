# histograms
counts = dict()
names = ['rush','wesh','uish','wesh','lack','rush','rush','lack']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)