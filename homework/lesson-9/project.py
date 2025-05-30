
import random

word_list = ['spain', 'japan', 'sudan', 'niger', 'malta', 'egypt' ]
our_word = random.choice(word_list)


def play_game(word,guess):
    feedback = []
    #our_letters = list(word)


    for i in range(5):
        if guess[i] == word[i]:
            feedback.append('🟩')
        elif guess[i] in word:
            feedback.append('🟨')
        else:
            feedback.append('⬛')

    return feedback
attempts = 6
print(" Welcome to Wordle! Guess the 5 letter word.")

for attempt in range(attempts):
    guess = input(f"Attempt {attempt+1}/{attempts} - Enter a 5 letter word: ").lower()

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
        print(f" You Lose! The word was: {our_word.upper()}")


'''import random

# List of words
word_list = ['spain', 'japan', 'sudan', 'niger', 'malta', 'egypt' ]
secret_word = random.choice(word_list)

max_attempts = 6

print("Welcome to Wordle! Guess the 5-letter word.")

for attempt in range(max_attempts):
    # Ensure input is valid (loops until a correct-length word is entered)
    while True:
        guess = input(f"Attempt {attempt + 1}/{max_attempts}: ").lower()
       
        if len(guess) == 5 and guess.isalpha():  # Check word length and alphabets
            break
        print("Invalid input! Enter a **five-letter word** containing only alphabets.")

    # Feedback for the guess using Wordle-style colored boxes
    feedback = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback.append(f"🟩 {guess[i].upper()} ")  # Correct position
        elif guess[i] in secret_word:
            feedback.append(f"🟨 {guess[i].upper()} ")  # Correct letter, wrong position
        else:
            feedback.append(f"⬜ {guess[i].upper()} ")  # Incorrect letter

    print("".join(feedback))  # Show feedback in Wordle format

    if guess == secret_word:
        print("🎉 Congratulations! You guessed the word correctly!")
        break
else:
    print(f"😢 Out of attempts! The correct word was '{secret_word}'.")'''


'''import random

# List of words
word_list = ['spain', 'japan', 'sudan', 'niger', 'malta', 'egypt' ]

def play_wordle():
    """Runs the Wordle game where users guess a secret 5-letter word."""

    secret_word = random.choice(word_list)
    max_attempts = 6

    print("Welcome to Wordle! Guess the 5-letter word.")

    for attempt in range(max_attempts):
        # Ensure input is valid (loops until a correct-length word is entered)
        while True:
            guess = input(f"Attempt {attempt + 1}/{max_attempts}: ").lower()
           
            if len(guess) == 5 and guess.isalpha():  # Check word length and alphabets
                break
            print("Invalid input! Enter a **five-letter word** containing only alphabets.")

        # Feedback for the guess using Wordle-style colored boxes
        feedback = []
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                feedback.append(f"🟩 {guess[i].upper()} ")  # Correct position
            elif guess[i] in secret_word:
                feedback.append(f"🟨 {guess[i].upper()} ")  # Correct letter, wrong position
            else:
                feedback.append(f"⬜ {guess[i].upper()} ")  # Incorrect letter

        print("".join(feedback))  # Show feedback in Wordle format

        if guess == secret_word:
            print("🎉 Congratulations! You guessed the word correctly!")
            break
    else:
        print(f"😢 Out of attempts! The correct word was '{secret_word}'.")

# Call the function to play
play_wordle()'''
