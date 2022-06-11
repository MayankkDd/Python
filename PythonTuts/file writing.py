# f = open("harry2.txt","w")
# f.write("Harry bahut acha ladka hai")
# f.close()

# f = open("harry2.txt","a")
# no_of_characters = f.write("Harry bahut acha ladka hai\n")
# print(no_of_characters)
# f.close()

# handle read and write both

f = open("harry2.txt", "r+")
print(f.read())
f.write("Harry bahur loolypop khata hai\n")
print(f.read())