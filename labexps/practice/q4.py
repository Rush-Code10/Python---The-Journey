# 1g Find the number of matching characters in two string

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

l=""

for i in range(len(s1)):
    for j in range(len(s2)):
        if s2[j] == s1[i]:
            if s2[j] not in l:
                l = l+s2[j]

print(print(l))
print(len(l))