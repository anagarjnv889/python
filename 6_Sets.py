# Sets contains unique value, unordered, mutable and ca store heterogenous element
s = set()
print(type(s))      # <class 'set'>
s ={1,2,3,4,5,1,2,3,55,8,6,7}       # {1, 2, 3, 4, 5, 6, 7, 8, 55} It will store unique value
print(s)

#________________________ Ste Functions____________
print("adding ele in set")
set ={1,2,3,4}
set.add(11)
print(set)      # {1, 2, 3, 4, 11}
set.add(11)
print(set)      # {1, 2, 3, 4, 11}
set.add("Ajay")
print(set)      # {1, 2, 3, 4, 'Ajay', 11}
# Deletion
print("removing ele from set")
set.remove("Ajay")
print(set)      # {1, 2, 3, 4, 11}
#set.remove(10)
#print(set)      # It element is not present then it will throw KeyError
print("using discard")
print(set)      # {1, 2, 3, 4, 11}
set.discard(2)
print(set)      # {1, 3, 4, 11} It will delete the element if it is there, otherwise it will do nothing
set.discard(10)
print(set)      # {1, 3, 4, 11}
# Update
print("adding the multiple element to set")
set.update([10,20,10])
print(set)      # {1, 3, 4, 10, 11, 20}
set.update((40,50,"Ajay"))
print(set)      # {1, 3, 4, 40, 10, 11, 50, 20, 'Ajay'}
#_________________________Set Operatins______________________________________________
#set union, set intersection, set diff and symmetric diff
print("Set operations")
print("Set Union")
a = {10,20,30,40}
b = {10,5,6,70}
print(a.union(b))   # {5, 70, 6, 40, 10, 20, 30} # print(a |b)
print(a |b)         # {5, 70, 6, 40, 10, 20, 30}
print(a," ",b)      # {40, 10, 20, 30}   {70, 10, 5, 6}
print("Set Intersection")
print(a.intersection(b))        # {10}
print(a & b)                    # {10}
print("Set Difference")
print(a.difference(b))          # {40, 20, 30}
print(a-b)                      # {40, 20, 30}
print("Set Symmetric diff")
print(a.symmetric_difference(b))    # {5, 70, 6, 40, 20, 30}
print((a | b) - (a & b))            # {5, 70, 6, 40, 20, 30}
#______________________________ Remove Dupliate from list_____________
print("Remove Dupliate from list")
lst = [10,20,10,3,4,4,5]
print(lst)
myset = set(lst)
print(myset)
mylst = list(myset)
print(mylst)


nums = set([1,2,4,1,2,3,3,4])
print(len(nums))

a={5,6,7,8}
b={7,5,6,8,9}
print(a==b)