str = "Hello World"
print(str, 'Length of str is',len(str) )
print(str[0:5])
print(str[0:12])
print(str[0:10])
# print all the charecter except last one
print(str[0:10])
print(str[0:-1])
print(str[:])       # It will print the whole string

# Step size
# str[start: end+1 : Step]
print("Step size")
print(str[0:11:2])
print(str[0:11:3])
print(str[11:0:-1])
# reverse the string
print(str[::-1])

# Some important op of String
s = "Welcome to Rajasthan"
print(s.lower())
print(s.upper())
print(s.title())        # It will return the string with first letter capital of each word
print(s.find("RAJ"))
print(s.find("Raj"))
print(s.split())        # It will splits the string with sapce and create a list
print(s.split('o'))     # It will splits the string with 'o' and create a list
replacestr = "Welcome to Mumbai"
print(s.replace(s, replacestr)   )    # Welcome to Mumbai
print(s)        # Welcome to Rajasthan
s = s.replace(s, replacestr)
print(s)        # Welcome to Mumbai

# strip  --> It will remove all the extra space from left and right.
# lstrip --> It will remove all the extra space from left.
# rstrip --> It will remove all the extra space from right.
st = "    Hello I am Ajay kumar nagar     "
print(st)
print(st.strip())
print(st.rstrip(), "Welcome to India")
print(st.lstrip(), "Welcome to India")
print('xyyzxxyxyy'.lstrip('xyy'))

# Concatenation of strings
s1 = "Ajay"
s2 = "Kumar"
s3 = "Nagar"
print(s1 + s2 + s3)

# split
s = "I am Ajay Kumar Nagar"
mys = s.split()
print(mys)        #  ['I', 'am', 'Ajay', 'Kumar', 'Nagar']
mys1 = "+".join(mys)
print(mys1)             # I+am+Ajay+Kumar+Nagar

# COunt no of vowels
int = " I aam ajay nagar"
count = 0
for ele in int:
    if(ele in "aeiouAEIOU"):
        count+=1
print(count)

# Palindrome string
pal = "madam"
palrev = pal[::-1]
if(pal == palrev):
    print("{} is a palindrome".format(pal))
else:
    print("{} is not a palindrome".format(pal))

# 2nd way
pal1 = "coding"
start = 0
is_palindrome1=  True
end = len(pal)
while(start<=end):
    if(pal1[start] != pal1[end]):
        is_palindrome1 = False
        break

    start +=1
    end -= 1
if(is_palindrome1):
    print("{} is a palindrome".format(pal1))
else:
    print("{} is not a palindrome".format(pal1))

# String important points
example = "coding_minutes"
print("%s" % example[3:7])
i = 5
j =4
i.__add__(j)
print(i)

x = "abcdef"
i = "a"
while i in x:
    x = x[:-1]
    print(x)
    print(i, end = " ")
print(5//2)

st = "HellO"
lower = ""
upper = ""
for i in st:
    if (i.islower()):
        lower = lower + i;
    else:
        upper = upper + i;
print(lower + upper)



# Write your logic here
s1 = "AJAaa"
s2 = "hjdbehjhgdyAJAaa"
n, m = len(s1), len(s2)
i, j = 0, 0
while (i < n and j < m):
    if (s1[i] == s2[j]):
        i += 1
    j += 1
if (i == n):
    print("True")
else:
    print("False")



