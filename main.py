import re
import random 

# Get the answer.
pool_file = open("HANGMAN SAM.txt")

pool_answers = []

pool_answer_line = pool_file.readline()

while pool_answer_line:
    pool_answers.append(pool_answer_line)

    pool_answer_line = pool_file.readline()

pool_file.close()

answer = random.choice(pool_answers)

answer = answer.upper()

# Pre-game setup.
answer_guessed = []

for current_answer_character in answer: 
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

#Game logic.
num_of_incorrect_guesses = 5

current_incorrect_guesses = 0

letter_guessed = []

# User gameplay logic.
while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guessed: 
    # Display game summary. 
    print(f"Number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}")

    print("Guessed letters: ", end="")

    for current_letter_guessed in letter_guessed:
        print(current_letter_guessed, end=" ")
    
    print()

    # Display puzzle board.
    for current_answer_index in range(len(answer)):
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], end="")
        else:
            print("_", end="")
    
    print()

    # Let user guess a letter.
    letter = input("Enter a letter: ")

    letter = letter.upper()

    # Check if user entered a valid letter.
    if re.search("^[A-Z]$", letter) and len(letter) == 1 and letter not in letter_guessed:
        #insert the letter guessed by the user (insertion sort)
        current_letter_index = 0 

        for current_letter_guessed in letter_guessed:
            if letter < current_letter_guessed:
                break
            
            current_letter_index += 1 
        
        letter_guessed.insert(current_letter_index, letter)

        # Check if letter is in puzzle. 
        if letter in answer:
            for current_answer_index in range(len(answer)):
                if letter == answer[current_answer_index]:
                    answer_guessed[current_answer_index] = True
        else:
            current_incorrect_guesses += 1 

# Post-game summary. 
if current_incorrect_guesses < num_of_incorrect_guesses:
    print ("Congratulations, you won!")
else:
    print (f"Sorry, you lost. The answer was {answer}")