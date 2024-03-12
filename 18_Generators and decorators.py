# Generators are like functions. It generated a sequence of value.
# Yiels keyword is used in generators
# Generators are faster and memory efficient
# Yield returns a valuse and pause the execcution while maintaining the internal states
def my_generator():
    n = 1
    print("First num")
    yield n

    n+=1
    print("Second num")
    yield n
    n+=1

my_generator1 = my_generator()
print(my_generator())           # <generator object my_generator at 0x000002672872C9C8>
print(next(my_generator1))      # First num     1
print(next(my_generator1))      # Second num    2
print("Executing counter method")
def counter(n):
    i =1
    while (i<=n):
        return i
        i = i+1

print(counter(5))

print("Executing counter method with Generatores(yeild)")
def counter(n):
    i =1
    while (i<=n):
        yield i
        i = i+1
ob = counter(5)
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))

# Generator with loop
print("Generator with loop")
for ele in counter(5):
    print(ele)

# Reverse string one by one with yeild

# Squares of number
# Square list
print("Square list of even numbers")
ele_list = [i**2 for i in range(1,100) if i%2==0]
print(ele_list)

# Square with the help of generator
print("Square with the help of generator")
ele_gen = (i**2 for i in range(100) if i%2!=0)
index = 0
for i in ele_gen:
    if index == 10:
        break
    print(i)
    index+=1

####################################################################################################################################################
# Decorators are just higher order functions
# Decorators can take function as argumnets
print()
print("Welcome to decorators")
# Higher oder functions
def add(ele):
    return ele+1

def sub(ele):
    return ele-1

def calculator(operator, number):
    result = operator(number)
    return result
print("This is a Addition function", calculator(add,5))
print("This is a subtract functions",calculator(sub,5))


# Function call inside function and returning of a functions
print("Function call inside function and returning of a functions")
print()
def inside():
    print("I am inside functions")

def add_features(fun):
    def ajay():
        print("I am Ajay functions")
        fun()
    return ajay

f = add_features(inside)
print(f())

# Decorative Call
print("Decorative call")
@add_features
def new_basic():
    print("I am new BAsic function")

new_basic()

