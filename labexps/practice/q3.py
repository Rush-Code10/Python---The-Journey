# Reverse A Number

num = int(input("Enter a number: "))
rev = 0
j = ""
while num!=0:
    digit = num%10
    j = j+str(digit)
    #rev=rev*10+digit
    num=num//10
print(rev)
print(j)