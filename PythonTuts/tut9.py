grocery= ["Harpic", "Glucose", "Biscuits", "Cloths", "Pen", 9467766333 ]
"""
print(grocery)
print(grocery[1])
print(grocery[1:6:2])
#print(grocery.sort())   # write it like just grocery.sort, No use to write print() function
#grocery.sort() # sort method is not applicable for the list which contains both instance of string and integer
print(grocery)
grocery.reverse()
print(grocery)
"""

# numbers=[10, 14, 8, 3, 9, 2, 18, 7]
"""
print(numbers[0:8:-2])
print(numbers[::-2])
print(numbers[-1::-2])
print(numbers[-1:-8:-2])
print(numbers[-1:8:-2])
print(numbers[-1:8:2]) # how this statement can give the output please illustrate ??
print(numbers[-1:4:2])
print(numbers[-1:4:-2])
"""
"""ok ok now i get why its giving the output coz we have to see the index here from -1th to 3rd
means it is considering the direction from right to left which is same as the direction when we see the number -2"""

#numbers.append(20)
"""
numbers.insert(5,35)
numbers.remove(9)
numbers.pop()
numbers.pop(4)
print(numbers)
"""
"""
#tuple
number= [2]
tp = (34, 69, 86, 96, 38, 59)
tp2 =(7)
tp3 =(7,)
# tp[1] = 47
print(number)
print(tp)
print(tp2)
print(tp3)
"""

a=1
b=8
a,b = b,a
print(a,b) # But how ??