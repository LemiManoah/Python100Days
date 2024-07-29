import random

word_list = ["banana", "enzyme", "alpine", "apple"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#create blanks for each letter in chosen word
display = []
for _ in chosen_word:
    display.append("_")



#guessing the letter
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("guess a letter: \n").lower()
    if guess in display:
        print(f"you have already guessed {guess}")
        
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    
    if guess not in chosen_word:
        print(f"you guessed {guess}, that is not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose, Game over")
    
    if "_" not in display:
        end_of_game = True
        print("you win")
