f= open("harry.txt","rt")
print(f.readlines())

# content = f.readline()
# print(content)

# print(f.readline())
# print(f.readline())

# content = f.read(344)
# print(content)

# for line in f:
#     print(line, end="")

# content = f.read(344)
# print(content)

f.close() # to free the resources used by the file , it is a good practise