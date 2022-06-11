# health management system
# 3 clients - Harry, Rohan and Hammad
# 6 files to be made in total for the clients to write (lock) and retrieve data from these files respectively for each
# client food and exercise


def getdate():
    import datetime

    return datetime.datetime.now()


current_date_time = "[" + str(getdate()) + "]"


def write_data_in_files(file_name):
    with open(file_name, "at") as f:
        f.write(current_date_time)
        f.write(" :   ")
        value = 1
        while value == 1:
            data = input("Enter the data\n")
            f.write(data)
            f.write(", ")
            value = int(input("Enter 1 to add more data and 0 to exit\n"))
            if value == 0:
                f.write("\n\n")
                break


def read_data_from_files(file_name):
    with open(file_name, "rt") as f:
        print(f.readlines())


client = input(
    "Enter the name of the client for which you want to write/retrieve the data : Harry, Rohan, Hammad\n"
)
activity = input(
    "Enter the name of activity for which you want to write/retrieve the data : Food, Exercise\n"
)
entr_retr = int(input("Enter 1 to write data or 2 to retrieve data\n"))

if entr_retr == 1:
    write_data_in_files(client + "_" + activity + ".txt")
elif entr_retr == 2:
    read_data_from_files(client + "_" + activity + ".txt")