str1='Python one';
str2="Python Two";
str3='''Python Three''';

print(str1)
print(str2)
print(str3)


print(str2[3])

# slicing in Python

lang = "programining"

print(lang[0:4])
print(lang[:8])

#---------Negative Slicing----------

fruit= "Apple"

print(fruit[-3:-1])


#-----------String Function----------

title="hi i am ashish kumar"

print(title.endswith("ari"))

print(title.capitalize())

print(title.replace('ashish',str(8)))

print(title.find("am"))

# Conditional Statment

marks=int(input("enter the marks:"))
print(type(marks))

if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=60:
    print("c")
else:
    print("F")