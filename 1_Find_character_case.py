c = input("Enter a character \n")
print(type(c))
if(c>='a' and c<='z'):
    print(c,"is Lower Case")
elif(c>='A' and c<='Z'):
    print(c,"is Upper case")
else:
    print("Please enter a character !!")