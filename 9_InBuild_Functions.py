# Abs, It will return the absolute value of arguments(Basically it will convert negative to positive)
print(abs(1.9))                 # 1.9
print(abs(-1.1))                # 1.1
print(abs(1))                   # 1
# Round, Round a number ato a given precision in decimal number || round(number, ndigit=None)
print(round(10.2457))           # 10
print(round(10.52))             # 11
print(round(10.2457, 2) )       # 10.25
#All, It will return true if numbers are positive or negative or Empty and it will return False for zero
list =[2,4,5,6]
print(all(list))                # True
list=[0,1,2,3]
print(all(list))                # False
list =[]
print(all(list))                # True
lst =[-10,-2]
print(all(lst))                 # True
lst =[-10,-2,0]
print(all(lst))                 # False
#Any It will return true if any number are present and it will return false if listor tuple is empty or zeros are there
print("Any in build")
lst =[10,2,3,4]
print(any(lst))                 # True
lst =[-10,2,3,4]
print(any(lst))                 # True
lst =[]
print(any(lst))                 # False
lst =[0]*5
print(any(lst))                 # False
lst =[-10,-2]
print(any(lst))                 # True
# Dir, Display all the function associated with an object
lst = [1,2,3,4]
print(dir(lst))                 # ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__']
# Aggregation Function
lst = [1,2,3,4,5]
print("sum is",sum(lst),"Max is",max(lst),"Min is",min(lst))    # sum is 15 Max is 5 Min is 1
