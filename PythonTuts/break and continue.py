"""
i=0
while(True):
    # i=i+1
    if i+1 < 5:
        i=i+1
        continue
    if (i == 10):
        break  # stop the loop
    print(i+1, end=" ")

    i=i+1
"""

while(True):
    number=int(input("Enter a number greater than 100 \n"))
    if number<100:
        print("Try Again!")
        continue
    print("congratulation you enter the number", number)
    break