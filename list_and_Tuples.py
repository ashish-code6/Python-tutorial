# List 

student=["Suresh","17","Python","Bangaluru"]

print(student)

print(student[2])

student[2]="JavaScript"

print(student)

#list is a immutable  
# in list also slicing is possible

#------- list In Method-------

list=[4,8,6,2,5]

#append method is used to add the value at the last list.

list.append(9);

#sorting in a List -------

list.sort()
#-----sorting a list in a reverse oreder-------
list.sort(reverse=True)


print(list.reverse())

list.reverse()

# add at particular index

list.insert(4,'a')

list.pop()
print(list)


#---------------Tuple-------------

#Tuple is mutable 

tuple=(4,69,6,8,9)
print(tuple)

print(type(tuple))

print("--------------")
print(tuple.index(6))

print(tuple.count(9))

#-------------
movieList=[];
movieOne=input("Enter Movie Name :")
# print(type(movieList))
movieList.append(movieOne);
movieTwo=input("enter second Movie Name:")
movieList.append(movieTwo);

print(movieList)



