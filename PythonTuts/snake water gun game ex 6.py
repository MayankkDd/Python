# snake water gun game
# played 10 times
# count the number of wins of user and computer

import random

def snake_water_gun() :

    # try:

        print("Welcome to 'snake water gun' game. You have 10 chances to play")
        computer_score = 0
        user_score = 0
        tie = 0

        for numberOfTurnsCounter in range(10):
            comp_option = ["s", "w", "g"]
            comp_choose = random.choice(comp_option)


            print("Enter your choice 's' for 'snake'\n 'w' for 'water'\n 'g' for 'gun'")
            user_choose = input()

            if comp_choose == "s":
                if user_choose == "s":
                    print("Its a tie")
                    tie += 1
                if user_choose == "w":
                    print("Computer Win!")
                    computer_score += 1
                if user_choose == "g":
                    print("You win!")
                    user_score += 1

            elif comp_choose == "w":
                if user_choose == "s":
                    print("You win!")
                    user_score += 1
                if user_choose == "w":
                    print("Its a tie!")
                    tie += 1
                if user_choose == "g":
                    print("Computer win!")
                    computer_score += 1

            elif comp_choose == "g":
                if user_choose == "s":
                    print("Computer win!")
                    computer_score += 1
                if user_choose == "w":
                    print("You win!")
                    user_score += 1
                if user_choose == "g":
                    print("Its a tie!")
                    tie += 1

        print("Your score = ", user_score)
        print("Computer Score = ", computer_score)
        print("Number of tie = ", tie)
        if computer_score > user_score:
            print("Computer wins this game!")
        elif computer_score == user_score:
            print("This game is a tie")
        else:
            print("****** You win this game ********")


    # except Exception as e:
    #     print(e)
    # print("Wrong input")

snake_water_gun()