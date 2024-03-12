# n=4
# 1
# 2 3
# 4 5 6
# 7 8 9 10
for i in range(2,10):
    print(i)
def pattern(n):
    a = 1
    for  i in range(n):
        for j in range(i+1):
            print(a,end=" ")
            a= a+1
        print()

if __name__ == '__main__':      # It can be accessed from out side the module
    n =int(input("Enter an interger"))
    pattern(n)

#_____________________________ Decimal To Binary___________________________________
def deciTobinary(n):
    list = []
    while(n>0):
        rem = n%2
        list.append(rem)
        n = n//2
    return list

n = int(input("Enter the number for binary conversion"))
list = deciTobinary(n)
list.reverse()
print(list)

#_______________________ Removing space from string O(n) ___________________________________________
def remove(s):
    output = ""
    for letter in s:
        #if letter != " ":
            output+=letter
    return output

s = input("Enter the string ")
print(remove(s))

#_______________________ Removing space from string O(1) ___________________________________________
def removeoptimised(s):
    output = []
    for letter in s:
        #if letter! = " ":
            output.append(letter)
    return "".join(output)
    return output

s = input("Enter the string ")
print(removeoptimised(s))
