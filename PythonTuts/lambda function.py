# def minus(a, b):
#     return (a-b)

# minus = lambda a,b: a-b
#
# print(" minus ", minus(9 ,4))
#
#
# def return_second_element(subject ):
#     return subject[1]

return_second_element = lambda subject :subject[1]

list_of_list = [ [1,5], [9,3], [6,11] ]

print(list_of_list)

list_of_list.sort(key = return_second_element) # here the key actually becomes is 5, 3, 11 coz retrun_second_element function
# will take [1,5] as an argument and then return second element i.e. 5

print(list_of_list)