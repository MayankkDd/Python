while(True):
    first_num = int(input("Enter first number\n"))
    second_num = int(input("Enter second number\n"))
    print(first_num, "is greater than ", second_num) if(first_num > second_num) else print(second_num, "is greater than ", first_num)
    n = int(input("Enter any number to and 0 to exit\n"))
    if (n==0):
        break