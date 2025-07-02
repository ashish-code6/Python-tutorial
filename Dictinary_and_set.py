#--------------Dictionary------------#
print("--------------Dictionary----------")

students={
    "name":"Mohit Kumar",
    "subject":{
        "phy":69,
        "Maths":86,
        "Computer":87
    },
    "sports":["Cricket","Football","Tennis"],
    "Hobbies":("music","Dance")
}
print(students)
print(type(students))

print(students["subject"]["phy"])