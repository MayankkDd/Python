# l = 10  # global
#
# def funtion1(name ):
#     # l = 20  # local
#     global l
#     print(l , "In funtion 1")
#
# funtion1("Passing to funtion 1")

x= 89
def harry():
    x=20
    def rohan():
        global x
        x= 80
    print("x value before calling rohan",x)
    rohan()
    print("x value before calling rohan",x)

harry()
print(x)