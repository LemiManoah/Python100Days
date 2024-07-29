#choosing a random number between 1 and 100
from random import randint

print("welocome to the guessing game")
print("I am thinking of a number between 1 and 100")
answer = randint(1, 50)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game():
#function for setting difficulty
    def set_difficulty():
        level = input("choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("invalid input")


    #function for checking the users guess
    def check_answer(guess, answer, turns):
        """checks guess against answer and keeps track of remaining turns"""
        if guess == answer:
            print("Congrats! You guessed the correct number!")
        elif guess > answer:
            print("Your guess is too high!")
            return turns -1
        else:
            print("Your guess is too low!")
            return turns - 1


    #let the user guess a number
    turns = set_difficulty()
    print(f"You have {turns} attempts to guess the correct number")

    #repeatedly ask for guess and check if the guess is equal to the answer
    guess = 0
    quit_game = False
    while guess != answer:
        guess = int(input("guess a number: "))
        #track the number of attempts left
        print(f"You have {turns} attempts to guess the correct number")
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of lives, you lose!")
            return
        elif guess != answer:
            print("Guess again")

game()