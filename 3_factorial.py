n = int(input("Enter the number \n"))
# fact = 1
# if n==0 or n==1:
#     print(n)
# else:
#     for i in range(2,n+1):
#         fact = fact*i
#     print(fact)

def fact(n):
    if n<0:
        return;
    elif n==0 or n==1:
        return 1
    return n*fact(n-1)

print(fact(n))