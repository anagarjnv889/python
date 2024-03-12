# Tuples are immutable, ordered and it contains heterogenous elelment
# There are only two function are there, Count and Index
# Faster than list
t =()                                               # t = tuple()
print(t)                                            # ()
tup = (8,10,"AJay",'Nagar',19.8)      
print(tup)                                          # (8, 10, 'AJay', 'Nagar', 19.8)

# we can create tuple with one element directly
tuple = ("ajay")
print(type(tuple))                                  # <class 'str'>

# For one element comma is mandatory
tuple =("ajay",)
print(type(tuple))                                  # <class 'tuple'>
tuple ="ajay",
print(type(tuple))                                  # <class 'tuple'>

print("Access element in tuples")                   #_______________ Access element in tuples_______________________________
print("Access element in tuples")
tuple =(10,20,45,86,"ajay")
print(tuple[0], tuple[4])                           # 10  ajay

print("Changing a tuple")                           #_______________ Changing a tuple________________________________________
lst = [10,20,"Nagar"]
tuple = (1,4,56,"Ajay", lst, 12.292)
print(tuple)                                        # (1, 4, 56, 'Ajay', [10, 20, 'Nagar'], 12.292)
tuple[4][-2] ="We did it"
print(tuple)            # (1, 4, 56, 'Ajay', [10, 'We did it', 'Nagar'], 12.292)

print("Tuple Function")                             #_______________ Tuple Functions ________________________________________

t = (10,20,30, "AJay",["PARAS",2])
for i in t:
    print(i, end=" ")
print()
for i in t:
    print(i*2, end=" ")
print()

#Concatinating Tuple
t = (1,2,3) + (4,5,6)
print(t)                                            # (1, 2, 3, 4, 5, 6)
print("Tuple Deletion")                             #_________________________# Tuple Deletion
# We can't chnage the element of tuple but we can delete the tuple
tdelete = (10,20,"Ajay")
print(tdelete)
del tdelete
#print(tdelete)                                     # Not Defined
print("Tuple Index")
t = (1,2,3,45,1)
print("index of 2", t.index(2))                     # It will reterun the index of the first occurence of element  # 1
print("Count of 3", t.count(3))                     # It will return the count for given number| for 3 it is 1
print("COunt of 4", t.count(4))                     # 0
print(9 in t)                                       # False
print("Tuple Unpacking")                            #___________________# Tuple Unpacking
t = (4,5,6,7)
print(*t)                                           # 4 5 6 7
a,b,c,d = t                                         # We have to give the equal no of variables, otherwise it will give an error
print(a,b,c,d)                                      # 4 5 6 7


a=(1,2,(4,5))
b=(1,2,(5,4))
print(a>b)                                         # False

a=(1,2)
b=(3,4)
c=a+b
print(c)                                            # (1, 2, 3, 4)

my_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
sorted_tuple = tuple(sorted(my_tuple))

print(sorted_tuple)
