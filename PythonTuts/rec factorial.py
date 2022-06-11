# def factorial_iterative(n):
#     """
#
#     :param n: input number
#     :return: n* (n-1)* (n-3)....  1
#     """
#
#     fac = 1
#     for i in range(n):
#         # print(i)
#         fac = fac * (i+1)
#     print (i)
#     return fac
#
# number = int(input("Enter the number\n"))
# factorial = factorial_iterative(number)
# print(factorial)


# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         print("va;ue of n before calculating factorial ", n)
#         n = n * factorial_recursive(n-1)
#         print ("value of n after calculating factorial", n)
#         return n
#
# number = int(input("Enter the number\n"))
# print("Factorial using recursive", factorial_recursive(number))


def fibonacci(n):
    temp = 0
    if n ==1:
        print("value of n when n==1 ", n)
        temp = 0
        print("returning value ", temp)
        return temp
    elif n==2:
        print("value of n when n==2 ", n)
        temp = 1
        print("returning value ", temp)
        return temp
    else :
        print ("value of n before calculating fibonacci addition ", n)
        n = fibonacci(n-2) + fibonacci(n-1)
        print("returning value in the last of the function", n)
        return n


number =  int(input("Enter the number to calculate nth fibonacci number\n"))
print("The number is : ", fibonacci(number))