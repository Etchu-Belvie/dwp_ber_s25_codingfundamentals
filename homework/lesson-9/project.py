'''
import random

word_list = ['spain', 'japan', 'sudan', 'niger', 'malta', 'egypt' ]
our_word = random.choice(word_list)


def play_game(word,guess):
    feedback = [''] * 5
    our_letters = list(word)


    for i in range(5):
        if guess[i] == our_word[i]:
            feedback[i] +='🟩'
        elif guess[i] in our_word:
            feedback +='🟨'
        else:
            feedback +='⬛'

    return feedback
attempts = 6
print(" Welcome to Wordle! Guess the 5 letter word.")

for attempt in range(attempts):
    guess = input(f"Attempt {attempt+1}/6 - Enter a 5 letter word: ").lower()

    if len(guess) != 5 or guess not in word_list:
        print("Invalid Word. Try again")
        continue

    feedback = play_game(our_word,guess)
    print(" ".join(guess.upper()))
    print("".join(feedback))

    if guess == our_word:
        print(" Congratulations! You Won")
        break
else:
        print(f" You Lose! The word was: {our_word.upper()}")'''
import random

WORD_LIST = ['apple', 'grape', 'mango', 'pearl', 'stone', 'climb', 'brave', 'flame', 'drink', 'fresh', 'video', 'wheel', 'plane', 'fruit']

solution = random.choice(WORD_LIST)

def give_feedback(guess, solution):
    result = []
    for i in range(5):
        if guess[i] == solution[i]:
            result.append('🟩')
        elif guess[i] in solution:
            result.append('🟨')
        else:
            result.append('⬛')
    return ''.join(result)

#Does not stop the user from entering the guess
def is_valid_guess(word):
    return len(word) == 5 and word.isalpha()

print("Welcome to Wordle in Python!")
attempts = 6

for attempt in range(attempts):
    guess = input(f"Attempt {attempt + 1}/{attempts} - Enter a 5-letter word: ").lower()
    
    if not is_valid_guess(guess) and  guess not in WORD_LIST:
        print("Word is not in list")
        continue

    feedback = give_feedback(guess, solution)
    print("Feedback:", feedback)

    if guess == solution:
        print("🎉 Congratulations! You guessed the word!")
        break
else:
    print(f"❌ Out of attempts! The word was: {solution}")


'''#Method 2 
#Does not accept an invalid input

import random

WORD_LIST = ['apple', 'grape', 'mango', 'pearl', 'stone', 'climb', 'brave', 'flame', 'drink', 'fresh', 'video', 'wheel', 'plane', 'fruit', 'lemon', 'fruit', 'poise', 'actor', 'earth', 'house', 'field']
solution = random.choice(WORD_LIST)

def give_feedback(guess, solution):
    result = []
    for i in range(5):
        if guess[i] == solution[i]:
            result.append('🟩')
        elif guess[i] in solution:
            result.append('🟨')
        else:
            result.append('⬛')
    return ''.join(result)

def is_valid_guess(word):
    return len(word) == 5 and word.isalpha()

print("Welcome to Wordle in Python!\n")
attempt = 1
max_attempts = 6

while attempt <= max_attempts:
    guess = input(f"Attempt {attempt}/{max_attempts} - Enter a 5-letter word: ").lower()

    if not is_valid_guess(guess):
        print("Word not in list.")
        continue

    if guess not in WORD_LIST:
        print("Word not in list.")
        continue

    feedback = give_feedback(guess, solution)
    print(" ".join(guess.upper()))
    print("".join(feedback))

    if guess == solution:
        print(" You guessed the word!")
        break

    attempt += 1

else:
    print(f" The word was: {solution}")'''
