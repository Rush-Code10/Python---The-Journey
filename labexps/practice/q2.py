#Tribonacci

n = int(input("No. of terms: "))

n1=0
n2=0
n3=1

print(n1,n2,n3,end=" ")

for i in range(0,n-3):
    n4 = n1+n2+n3
    n1=n2
    n2=n3
    n3=n4
    print(n4,end=" ")
