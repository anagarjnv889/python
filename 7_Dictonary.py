# Store data in key and pair value, unordered, unindexabledic, access the value with keys, Mutable, It will directly search for key(o(1))
dic = dict()
print((type(dic)))              # <class 'dict'>
print("create a dictonary with the list of tuple")  # create a dictonary with the list of tuple
mydict = dict([(1, "Ajay"),  (3, "Nagar")])
print(mydict)                   # {1: 'Ajay', 3: 'Nagar'}
my_dic  = {
    "Name" : "Ajay",
    "age" : 23,
    "5" : 7.9
}
print(my_dic)                   # {'Name': 'Ajay', 'age': 23, 'grades': 7.9}
# Accessing Element
print(my_dic['age'])            # 23
# unknown key will give us an keyerror, we can avoid that error my using my_dict.get("hobby")
#print(my_dic['hobby'])         # KeyError
print(my_dic.get("hobby"))      # None
# Add/Modify data in dictionary
print(my_dic)
my_dic['hobby'] = ['Football', 'Reading']
my_dic['Lname'] = 'Nagar'
my_dic['LTTS_Grade'] = 2
print(my_dic)                   # {'Name': 'Ajay', 'age': 23, 'grades': 7.9, 'hobby': ['Football', 'Reading'], 'Lname': 'Nagar', 'LTTS_Grade': 2}
print(my_dic.get('hobby'))      # ['Football', 'Reading']
my_dic['LTTS_Grade'] = 3
print(my_dic)                   # {'Name': 'Ajay', 'age': 23, 'grades': 7.9, 'hobby': ['Football', 'Reading'], 'Lname': 'Nagar', 'LTTS_Grade': 3}
# Dictionary Functions
# Display all keys
print("Display all keys")
print(my_dic.keys())            # dict_keys(['Name', 'age', 'grades', 'hobby', 'Lname', 'LTTS_Grade'])
print(list(my_dic.keys()))      # ['Name', 'age', 'grades', 'hobby', 'Lname', 'LTTS_Grade']
# display all values
print("display all values")
print(my_dic.values())            # dict_values(['Ajay', 23, 7.9, ['Football', 'Reading'], 'Nagar', 3])
print(list(my_dic.values()))      # ['Ajay', 23, 7.9, ['Football', 'Reading'], 'Nagar', 3]
# display (key, Values pair in tuple
print(my_dic.items())
print(list(my_dic.items()))     # [('Name', 'Ajay'), ('age', 23), ('grades', 7.9), ('hobby', ['Football', 'Reading']), ('Lname', 'Nagar'), ('LTTS_Grade', 3)]
# Iter
print("print one by one")
for key, val in my_dic.items():
    print(key, ":", val)
# print one by one
# Name : Ajay
# age : 23
# grades : 7.9
# hobby : ['Football', 'Reading']
# Lname : Nagar
# LTTS_Grade : 3
print("Direct iterable")
for ele in my_dic:
    print(ele)      # It will return the keys
#Name
#age
#grades
#hobby
#Lname
#LTTS_Grade
print("Direct iterable with values")
for ele in my_dic:
    print(my_dic[ele])
#Ajay
# 23
#7.9
#['Football', 'Reading']
#Nagar
#3
print("Key and values together")
for ele in my_dic:
    print(ele,":", my_dic[ele])
#Name : Ajay
#age : 23
#grades : 7.9
#hobby : ['Football', 'Reading']
#Lname : Nagar
#LTTS_Grade : 3
# In keys we can take only immutable(int, strings, tuple) but not list, dict and set(mutable)
print(hash(556))        # 556
print(hash("ajay"))     # -2651515078666184919
#hash([1,2,4])          # unhashable type
# Delete element from dictionary | Key should be present
print("Delete element from dictionary")
# mt_dic.pop(key)  It will return the values of that key and delete it.
d = {"Name" : "ajay", "Comapny" : "LTTS", 1 : 3}
print(d)                # {'Name': 'ajay', 'Comapny': 'LTTS', 1: 3}
print(d.pop(1))         # 3
print(d)                # {'Name': 'ajay', 'Comapny': 'LTTS'}
print(d.pop('Name')," ", d)     # ajay   {'Comapny': 'LTTS'}
# delete age
del my_dic['age']
print(my_dic)           # {'Name': 'Ajay', 'grades': 7.9, 'hobby': ['Football', 'Reading'], 'Lname': 'Nagar', 'LTTS_Grade': 3}
# Neste Dictionary
print("Nested Dictionary")
menu = {
    'samosa' : 10,
    'pizza' : 100,
    'fruits' : {
        'apple' : 100,
        'grapes' : 50,
        'banana' : 20
    }
}
print(menu)             # {'samosa': 10, 'pizza': 100, 'fruits': {'apple': 100, 'grapes': 50, 'banana': 20}}print(menu['pizza'])    # 100
print(menu['fruits']['banana']) # 20
menu['juice'] = [20,30,40]
print(menu)             # {'samosa': 10, 'pizza': 100, 'fruits': {'apple': 100, 'grapes': 50, 'banana': 20}, 'juice': [20, 30, 40]}
# Create a new dictionary with only pairs hwere the value is larger than 2
a = {'a': 1, 'b':2, 'c':3}
n = { k:v for k,v in a.items() if v>2}
print(n)        # {'c': 3}
n1 = { k+"z" : v**2 for k,v in a.items() if v>2}
print(n1)       # {'cz': 9}
print("reverse of the dictionary")              # Reverse the dictionary
di = {'a' : 1, 'b' : 2, 'c' : 3, 'd':4}
print(di)       # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
rev_d = dict()
for k, v in di.items():
    rev_d[v] = k
print(rev_d)        # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
