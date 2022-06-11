# health management system
# 3 clients - Harry, Rohan and Hammad
# 6 files to be made in total for the clients to write (lock) and retrieve data from these files respectively for each
# client food and exercise

def getdate():
    import datetime
    return datetime.datetime.now()

current_date_time = "[" + str(getdate()) + "]"  # converting return value to string type

def write_data_in_files(file_name ):
    with open(file_name,"at") as f:
        f.write(current_date_time)
        f.write(" :   ")  # or this can be written as:- f.write("[" + str(gettime()) + "]" + " :  "
        value = 1
        while value == 1:
            data = input("Enter the data\n")
            f.write(data + ", ")
            print("Item added successfully")
            # f.write(", ")

            value = int(input("Enter 1 to add more data and 0 to exit\n"))
            if value == 0:
                f.write("\n\n")
                break

def read_data_from_files(file_name ):
    with open(file_name,"rt") as f:
        print(f.readlines())


client = input("Enter then name of the client for which you want to write/retrieve the data : Harry, Rohan, Hammad\n")
activity = input("Enter the name of activity for which you want to write/retrieve the data : Food, Exercise\n")
entr_retr = int(input("Enter 1 to write data or 2 to retrieve data\n"))

if(entr_retr == 1):
    if client == "Harry" and activity == "Food":
        file_name = "Harry_food.txt"
        write_data_in_files(file_name)
    elif client == "Harry" and activity == "Exercise":
        file_name = "Harry_exercise.txt"
        write_data_in_files(file_name)
    elif client == "Rohan" and activity == "Food":
        file_name = "Harry_exercise.txt"
        write_data_in_files(file_name)
    elif client == "Rohan" and activity == "Exercise":
        file_name = "Harry_exercise.txt"
        write_data_in_files(file_name)
    elif client == "Hammad" and activity == "Food":
        file_name = "Harry_exercise.txt"
        write_data_in_files(file_name)
    elif client == "Hammad" and activity == "Exercise":
        file_name = "Harry_exercise.txt"
        write_data_in_files(file_name)
elif (entr_retr ==2):
    if client == "Harry" and activity == "Food":
        file_name = "Harry_food.txt"
        read_data_from_files(file_name)
    elif client == "Harry" and activity == "Exercise":
        file_name = "Harry_exercise.txt"
        read_data_from_files(file_name)
    elif client == "Rohan" and activity == "Food":
        file_name = "Harry_exercise.txt"
        read_data_from_files(file_name)
    elif client == "Rohan" and activity == "Exercise":
        file_name = "Harry_exercise.txt"
        read_data_from_files(file_name)
    elif client == "Hammad" and activity == "Food":
        file_name = "Harry_exercise.txt"
        read_data_from_files(file_name)
    elif client == "Hammad" and activity == "Exercise":
        file_name = "Harry_exercise.txt"
        read_data_from_files(file_name)
else:
    print("Wrong input, Please try again")
