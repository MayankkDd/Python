"""
list1=  [ ["himanshu",51], ["honey",42], ["sachin",7], ["janit",36] ]
print(list1)
dict1 = dict(list1)
print(dict1)
for item, rollno in list1:
    print(item,"roll number is", rollno )

for item, rollno in dict1.items():
    print(item, "roll number is", rollno)

for item in dict1:
    print(item)
"""

list2 = ["himanshu","sachin","janit","himanshu", 51, 42, 7, 2, 8, 4, 6, 54, 73]

for item in list2:
    if str(item).isnumeric() :
        if item > 6:
            print(item)