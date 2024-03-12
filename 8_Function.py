# Reusability of code | Functions are not associated with class and object, we can take as many as arguments|
# |Methods are associated with class and object. These are in build like append, sort()|
def greetings(name):
    print("Welcome",name)

greetings("Ajay")                           # Welcome Ajay
greetings(10)                               # Welcome 10
print(greetings)                            # <function greetings at 0x00000266CF79C1E0>
print(type(greetings))                      # <class 'function'>
print("Addition of two numbers")            # Addition
def add(a,b):
    '''It will return addition of two number'''
    return a+b
print(add(10,20))

print("Sum of list element")              # Sum of list element
def sum(list):
    s = 0
    for i in list:
        s = s+i
    return s
list = [1,2,3,4]
print(sum(list))                          # 10
# FUNCTION CAN RETURN MULTIPLE VALUES IN FORM OF A TUPLE
def calculator(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a//b
    return sum, sub, mul,div    # (12, 8, 20, 5)
    # We can also use   return [sum, sub, mul,div ]  and output is  [12, 8, 20, 5]
print(calculator(10,2))

# Scope of Variable
# Global Variables :- Variables that are created outside of a function, Global variables can be used by anywhere in the program. print(globals)
# Local Variable :-   Variables that are created inside a function, Local variables can't be used outside the function.

r = 100
def testfun():
    global r
    r = 200
    print(r)        # 200
testfun()
print(r)            # 200

# Lambda Function  || lambda a, b: a+b
print("lambda function")
add = lambda a, b: a+b
print(add(10,20))   # 30
print(add)          # <function <lambda> at 0x000001668E2D3378>

func = (lambda x, y : x+y if x+y>0 else 0)
print(func(10, 2))      # 12
# LCM of two numbers using function
def lcm(a, b): # Parameters
    max_num = (a if a>b else b)
    while True:
        if((max_num % a== 0) and (max_num % b== 0)):
            return max_num
        else:
            max_num = max_num+1
print(lcm(10,2)) # Argumnets
# Arguments lcm(10,20)

# Positional Arguments
def pos(name, country):
    print("Hello I am",name,"and I am from",country)
pos("Ajay","India")     # Hello I am Ajay and I am from India
# we can give like this pos("Ajay")

# Default Argumnets
def pos(name, country = 'UK'):
    print("Hello I am",name,"and I am from",country)
pos("Ajay")             # # Hello I am Ajay and I am from UK
pos("Ajay","US")             # # Hello I am Ajay and I am from US

def pos(name, country):
    print("Hello I am",name,"and I am from",country)
pos("Ajay","India")

# Arbitary Arguments
# It can rececive any no of arg and store them in a tuple
def art(*args):
    print(args)
art(10,10,20,"aJAY","True",True)        # (10, 10, 20, 'aJAY', 'True', True)
# Keyword Arguments
# It can rececive any no of arg and store them in a dictonary and parameter name is mandatory while calling function
def key(**args):
    print(args)
    print(args['name'])     # AJay
key(name="AJay", age= 24, country = "India")        # {'name': 'AJay', 'age': 24, 'country': 'India'}
# More about Keyword argumnets
def key(**args):
    print(args)       # {'name': 'AJay', 'age': 24, 'country': 'India', 'hobby': ['football', 'Coding', 20]}
    for k,v in args.items():
        print(k,":",v)
key(name="AJay", age= 24, country = "India", hobby =["football", "Coding", 20])
# name : AJay
# age : 24
# country : India
hobby : ['football', 'Coding', 20]

#
def key(a,b,c,age =24, *args, **arg):
    print(a,b,c,age)
    print(args)
    print(arg)

key(10,20,30,50,100,200, x="AJay", y=21, company =["LTTS","LTI"])
# Output
# 10 20 30 50
# (100, 200)
# {'x': 'AJay', 'y': 21, 'company': ['LTTS', 'LTI']}

def foo(i, x=[]):
    x.append(i)
    return x


for i in range(3):
    print(foo(i), end=" ")


def foo(i, x=[]):
    x.append(x.append(i))
    return x


for i in range(3):
    y = foo(i)

print(y)


def foo(x):
    x[0] = ['def']
    x[1] = ['abc']
    return id(x)


q = ['abc', 'def']
print(id(q) == foo(q))
