# f = open("harry.txt")
# print(f.readlines())
# print(f.tell())
# print(f.readline())
# f.close()

with open("harry.txt") as f:
    a=f.read(5)
    print(a)
    # print(f.tell)
    print(f.readline())