# Many form
# Operator polymorphism
a = "Hello"
b = "World"
print(a+b)      # HelloWorld
a =10
b = 5
print(a+b)      # 15
a =[1,2,4]
b = [3,5,6]
print(a+ b)     # [1, 2, 4, 3, 5, 6]


# Write only the classes and their member functions.
# No need to initialize and call functions.

# Write only the classes and their member functions.
# No need to initialize and call functions.


class SchoolMember:
    ### Write Code for SchoolMember class ###
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return "My name is {}. I am {} years old".format(self.name, self.age)
    ### Code ends here ###


class Student(SchoolMember):
    def __init__(self, my_class, roll_no):
        self.my_class = my_class
        self.roll_no = roll_no

    def introduce(self):
        return "I am in {} class. My roll number is {}".format(self.my_class, self.roll_no)


class Teacher(SchoolMember):
    def __init__(self, subject, salary):
        self.subject = subject
        self.salary = salary

    def introduce(self):
        return "I Teach {} subject. My salary is {}".format(self.subject, self.salary)


ob = SchoolMember("Prateek", 27)
print(ob.introduce())
ob1 = Teacher("Physics", 10000)
print(ob1.introduce())
ob2 = Student("SIx", 6)
print(ob2.introduce())





