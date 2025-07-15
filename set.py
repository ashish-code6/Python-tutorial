#---------Set in Python-------
thisset={"apple","orange","Mango"}
print(thisset)
print(type(thisset))

#Set items are unordered, unchangeable, and do not allow duplicate value.

thisset1 = {"apple","apple", "banana", "cherry", True, 1, 2}

print(thisset1)

#Get the Length of a Set
#To determine how many items a set has, use the len() function.

print(len(thisset1))


#Python - Access Set Items

name={"a","b","ap","tl"}

for i in name:
    print(i)

print("k" in name)

thisset.update(name)
print(thisset)