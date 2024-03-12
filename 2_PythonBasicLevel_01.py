# Nested if else
n = 10
if n > 0:
    print(n,"is a positive number")
elif(n<0):
    print(n," is a negative number")
else:
    print(n," is neither positive nor negative")

# Loops in Python(For and While)
a = 5
while a>0:
    print(a, end = "`, ")
    a = a-1
print()
for i in range (2, 10):
    print(i, end = ", ")
print()
for i in range (2, 10, 2):
    print(i, end = ", ")

# Break, Continue and Pass
# Break
print("Break statment")
for i in range(1, 10):
    if(i==5):
        break
    print(i)
else:
    print("No element left")

print("Continue Statement")
for i in range(1, 10):
    if(i==5):
        continue
    print(i)
else:
    print("No element left")


for l in 'Jhon':
    if l == 'o':
        pass
    print(l, end=", ")


# Prime Number Program
print()
a = int(input("Enter an Integer"))
is_prime = True
for i in range(2, a//2):
    if(a%i==0):
        is_prime = False
if(is_prime):
    print("{} is a prime number".format(a))
else:
    print("{} is not a prime numner".format(a))

