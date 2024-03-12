import math
n = int(input("Enter the number \n"))
def prime(n):
    if(n<=1):
        return
    flag = True
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            flag = False
            break
    return flag

if prime(n):
    print(n,"is a prime number")
else:
    (print(n,"is not a prime number"))
