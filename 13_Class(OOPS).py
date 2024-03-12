# Class is a user defined blueprint or protocol of a real world entity. Classes can be treated as datatype
# Object are the instance of the class. Object can be treated as variable
class Human:
    print("Hello welcome to OOP's Class")
mohit = Human()
print(type(mohit))          # <class '__main__.Human'>
# Constructor is a special memeber function of a class.

class Ajay:
    def __init__(self):         # #constructor is used to assign values to the newly created objects.
        print("creating new object")
a = Ajay()
print("Nagar class output")

class Nagar:
    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age
        print("I am", name,"and my age is",age)
a = Nagar("Ajay",23)        # I am Ajay and my age is 23
print(a.name)               # Ajay


# Using function
class viki:
    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age
        print("Object created")

    def introduce(self):
        return "I am {} and my age is {}".format(self.name, self.age)

    def introduce1(self, name, age):
        return "I am {} and my age is {}".format(name, age)

h1 = viki("AJAY", 23)       # Object created
print(h1.introduce())       # I am AJAY and my age is 23
h2 = viki("NAGAR", 24)
print(h2.introduce1("NAGAR", 24))   # I am NAGAR and my age is 24
# You can change the value of object
h2.name ="Jatib"
print(h2.name)

# Class Variables
print("Now we will talk about class variables")
class viki:
    # Class Variable
    lst = [10,20,30,40,50]
    id = 101
    population = 0
    database = []
    def __init__(self, name, age, is_alive = True):
        # instance variable
        self.name = name
        self.age = age
        self.is_alvie = is_alive
        self.id = viki.id
        self.population = viki.population
        viki.id +=1
        viki.population +=1
        viki.database.append(self)
        print("Object created")

    def introduce(self):
        return "I am {}. My age is {} and my id is {}".format(self.name, self.age,self.id)

    def die(self):
        if self.is_alvie:
            print(self.name, "is dying......")
            self.is_alvie = False
            viki.population -= 1

h1 = viki("AJAY", 23)       # Object created
print(h1.introduce())       # I am AJAY and my age is 23
h2 = viki("Nagar", 24)      # Object created
print(h2.introduce())       # I am Nagar. My age is 24 and my id is 102
h3 = viki("Paras", 27)      # Object created
print(viki.population)      # 3
print(h1.die())             # I am Nagar. My age is 24 and my id is 102
print(viki.population)      # 2
print(viki.database)        # [<__main__.viki object at 0x000001D0F7169320>, <__main__.viki object at 0x000001D0F7169390>, <__main__.viki object at 0x000001D0F7169358>]
print(viki.lst)             # [10, 20, 30, 40, 50]
print(viki.id)              # 104





class Demo:
    def __init__(self):
        pass

    def test(self):
        print(__name__)


obj = Demo()
obj.test()


class change:
    def __init__(self, x, y, z):
        self.a = x + y + z


x = change(1, 2, 3)
y = getattr(x, 'a')
setattr(x, 'a', y + 1)
print(x.a)


class demo():
    def __repr__(self):
        return '__repr__ function called'

    def __str__(self):
        return '__str__ function called'


s = demo()
print(s)
