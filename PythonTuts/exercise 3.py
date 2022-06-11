# number =18
# no of guesses =6
# no of guesses left
# no of guesses he took to finish
# game over

number = 18
no_of_guess_taken = 0
print("Number of guesses you have : 6")
print("Find a hidden number between 1 to 25")

while(True):
    guess = int(input())
    no_of_guess_taken =no_of_guess_taken +1
    if(guess==18):
        print("Congratulation you found number",number)
        print("Number of guesses you took to finish", no_of_guess_taken)
        print("Numer of guesses remaining : ", 6 - no_of_guess_taken)
        print("Game Over!!")
        break
    elif guess > 18:
        print("Hidden number is lesser than ", guess)
    elif guess < 18:
        print("Hidden Number is greater than ", guess)
    print("Numer of guesses remaining : ", 6-no_of_guess_taken)