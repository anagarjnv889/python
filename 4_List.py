# Ordered collection of element || Mutable and can store heterogenous elements

# creating an empty list
mylst = [10, 20, 30, 40]
print(mylst)        #[10, 20, 30, 40]

# Indexing/Slicing of List works same ass Strings
print(mylst[0], " ", mylst[-1])     # 10   40
print(mylst[1:-1])      # [20, 30]
print(mylst[::-1])    # Reverse of a list [40, 30, 20, 10]
print(mylst[::1])       #[10, 20, 30, 40]
print(mylst[::2])       #[10, 30]
print(mylst[::-2])      #[40, 20]

# Changing list
print("My original list ", mylst)        # My original list  [10, 20, 30, 40]
mylst[1] = "Ajay"
print(mylst)        #[10, 'Ajay', 30, 40]

# Important method for list
list = ["Ajay", 10, 20, 50, "Nagar"]      # ['Ajay', 10, 20, 50, 'Nagar']
print(list)
# Append at the given element to end of list | append(value)
list.append(100)
print(list)     # ['Ajay', 10, 20, 50, 'Nagar', 100]
list1 = ["Ajay", 10, 20, 50, "Nagar"]
list1.append(["I", "Love", "JNV"])
print("List 1 is :", list1)     # ['Ajay', 10, 20, 50, 'Nagar', ['I', 'Love', 'JNV']]

# Insert, It will insert the given element at given index | insert(index, value)
list.insert(1, "Kumar")
list.insert(7, 200)
print(list)     # ['Ajay', 'Kumar', 10, 20, 50, 'Nagar', 100, 200]

# Pop, It will delete the last element of list and It will return that element | pop()
# Pop function can also take index if you want to delete a particular element | pop(index)
print("List before pop function ", list)    # ['Ajay', 'Kumar', 10, 20, 50, 'Nagar', 100, 200, 600]
ele = list.pop()
print("Deleted element from list id :", ele)    # Deleted element from list id : 200
print(list)     # ['Ajay', 'Kumar', 10, 20, 50, 'Nagar', 100]
index= 4
ele = list.pop(index)
print("Deleted element from",index," index is :",ele)   # Deleted element from 4  index is : 50
print(list)     # ['Ajay', 'Kumar', 10, 20, 'Nagar', 100]

# Remove, Remove first occurrence of value | remove(value)
removelist = ["Ajay", 10, 20, 10, "Ajay"]
print("List before remove method",removelist)    # List before remove method ['Ajay', 10, 20, 10, 'Ajay']
removelist.remove("Ajay")
removelist.remove(10)
print(removelist)       # [20, 10, 'Ajay']

# Reverse a list
reverselist =  ["Ajay", 10, 20, 30, "Nagar"]
reverselist.reverse()
print(reverselist)      # ['Nagar', 30, 20, 10, 'Ajay']

# Sort a list in both directions
sortlist =  [10,40,28,5,100,30]
sortlist.sort()
print(sortlist)     # [5, 10, 28, 30, 40, 100]
sortlist.sort(reverse=True)
print(sortlist)     # [100, 40, 30, 28, 10, 5]

# Extend, extend(iterable)
list1 = ["Ajay", 10,20,50, "Nagar"]
list1.append(["I", "Love", "JNV"])
print("List 1 is :", list1)     # ['Ajay', 10, 20, 50, 'Nagar', ['I', 'Love', 'JNV']]
list1.extend([10,20,30])
print(list1)        # ['Ajay', 10, 20, 50, 'Nagar', ['I', 'Love', 'JNV'], 10, 20, 30]

# Copy a list
a =[1,2,3,4,5]
b = a
b.append(6)
print("a list is : ",a)     # a list is :  [1, 2, 3, 4, 5, 6]
print("b list is: ", b)     # b list is:  [1, 2, 3, 4, 5, 6]
# we are just refernecing the same list, we should use list.copy()
c =[1,2,3,4,5]
d = c.copy()
d.append(6)
print("c list is : ",c)     # c list is :  [1, 2, 3, 4, 5]
print("d list is: ", d)     # d list is:  [1, 2, 3, 4, 5, 6]
######################################### 2D List #########################################
list_2D = [[1,2,3], [4,5,6], [7,8,9]]
print(list_2D)      # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing 2D list
print(list_2D[2][1])        # 8
print(list_2D[-1][-2])      # 8

# Adding two 2D list
A = [[1,2], [3,4]]
B = [[5,6], [7,8]]
C = [[None, None ], [None , None ]]
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]
print(C)        # [[6, 8], [10, 12]]

print([[None]*5] * 5)

q =[1,2,3,4,5]
# 5 1 2 3 4     # 4 5 1 2 3     # 3 4 5 1 2     # 2 3 4 5 1     # 1 2 3 4 5
l =len(q)
for i in range(l):
    ele = q.pop()
    q.insert(0,ele)
    print(q)
    print()

# Not is not allowed in python for loops
#a = [0, 1, 2, 3]
#i = -2
#for i not in a:
#    print(i)
#    i += 1


a = [0, 1, 2, 3]
for a[-1] in a:
    print(a[-1])

l =[10, 20,"ajay"]+["Nagar", 20]
print(l)
la=[10,20,10,50,30,20]
a=sorted(la)
print(a)
