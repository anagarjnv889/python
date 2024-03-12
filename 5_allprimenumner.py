import math
n = int(input("Enter the number till whcih you want to find the prime number\n"))
def prime(n):
    if(n<=1):
        return
    flag = True
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            flag = False
            break
    return flag

print("prime numbers are")
for i in range(n+1):
    if prime(i):
        print(i)