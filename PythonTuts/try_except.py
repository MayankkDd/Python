# the benefit of this try exception approach is the code will keep on running it won't through any error
# and come to hault because of an error or exception you can say

print("Enter first number")
num1= input()
print("Enter second number")
num2= input()
try:
    print("Sum of first and second number is ", int(num1) + int(num2))
except Exception as e:
    print(e)
print("This is very important line of code")