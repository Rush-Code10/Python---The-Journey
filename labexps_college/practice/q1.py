#Fibonacci

n = int(input("No. of terms: "))

n1 = 0
n2 = 1

print(n1, n2, end=" ")

for i in range(0,n-2):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3,end=" ")