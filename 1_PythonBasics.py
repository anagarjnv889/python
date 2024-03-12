print(5//2)     # It will return integer values // 2
print(5//2)     # It will return float values // 2.5
print(5//2)     # It will return  values // 1

print('I am', 'Ajay', 'Kumar',1)    # I am Ajay Kumar 1
a = 10
s = 'Ajay'
# Type of variable
print(type(a), type(s))
# Location of variable
print(id(a))
print(id(s))

# Basic datatype in python
intnum = 10
floatnum = 10.2565
a = 10 + 2j
print(intnum,floatnum,a)    # 10 10.2565 (10+2j)
print(type(a))              # <class 'complex'>
truebool, falsebool= True, False    # Boolean: Python -> True and False, Java -> true and false
print(truebool, falsebool)
none = None                 # None type
print(none)


# How take input from user in python
# input()  It always return string value
#takeinput = input("Enter the input ")
print("User entered : ",takeinput, "data type of the input : ",type(takeinput))

# Type Casting
a = 10
print(type(a))
a = str(a)
print(a)
print(type(a))
a = float(a)
print(a)

# Multiline
multilineVariable = 1 + 2 + 3 \
    + 4 + 5 + 6 +100+\
    7 + 8 + 9
print("Value of multilineVariable : ",multilineVariable)    # Value of multilineVariable :  145

# Output formatting
name = "Ayon"
message = "Daaru Piyega"
name1= "Srikar"
message1 = "Haan bhai"
print("{} : {} {}".format(name,message,name1))  # Ayon : Daaru Piyega Srikar
print("{} : {} {}".format("name",message,name1))  # name : Daaru Piyega Srikar
print("{} : {}".format(name1,message1))         # Srikar : Haan bhai
print("Hello {n} : bol {m}".format(n=name, m=message))  # Hello Ayon : bol Daaru Piyega

# Special Operator
# Membership Operator(in) Not Applicable for int, float.....
mystr = "Ajay Kumar Nagar"
print("Nagar is in Ajay Kumar Nagar : ", "Nagar" in mystr) # Nagar is in Ajay Kumar Nagar : True

# Is operator(It will check the location)
a=5000
b=5000
print(a is b)               # True
c=500
print(c is b)               # False
mystr = "Ajay Kumar Nagar"
mystr1 = "I am Ajay Kumar Nagar"
print("mystr is same as mystr1 :",mystr is mystr1)      # mystr is same as mystr1 : False
print(mystr in mystr1)      # True
