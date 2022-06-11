def get_and_print_string_function(string):
    return f"Ye string function hai tutmain1 ka jo ki return ker reha hai string: {string}"

def defaulter_add_funtion(num1, num2):
    # print("returning defaulter sum : " )
    print("the value of __name__ in tutmain1 file is", __name__)
    return ("returning defaulter sum : " , num1 + num2 + 5)



print("the value of __name__ in tutmain1 file is", __name__)

if __name__ == '__main__':
    print(get_and_print_string_function("Harry1"))
    result = defaulter_add_funtion(4, 6)
    print(result)