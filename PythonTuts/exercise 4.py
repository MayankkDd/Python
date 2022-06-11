# patten printing from stars for taking a value of where n is the number of rows
# press 1 to print it in increasing order and 1 to print it in decreasing order

try:
    number_of_rows= int(input("Enter the number of rows \n"))
    print("Press 1 to print in increasing order and 0 to print in decreasing order")
    temp = int(input())
    value = bool(temp)

    # if (value==1):
    #     order_value= "True"
    # else:
    #     order_value= "False"

    if(value==True):
        row_number = 1
        while(row_number <= number_of_rows):
            column_number = 1
            while(column_number <= row_number):
                print("*", end ="")
                column_number = column_number + 1
            print("")
            row_number = row_number + 1
    if(value==False):
        row_number = 1
        temp = 1
        while (row_number <= number_of_rows):
            column_number = 1
            while (column_number <= (number_of_rows+1 - temp)):
                print("*", end="")
                # print("column_number ", column_number, "temp ", temp, end="")
                column_number = column_number + 1
            temp = temp + 1
            print("")
            row_number = row_number + 1
except Exception as e :
    print("invalid input")