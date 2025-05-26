
import random

word_list = ['spain', 'japan', 'sudan', 'niger', 'malta', 'egypt' ]
our_word = random.choice(word_list)


def play_game(word,guess):
    feedback = [''] * 5
    our_letters = list(word)


    for i in range(5):
        if guess[i] == word[i]:
            feedback[i] += 'GREEN'
        elif guess[i] in our_word:
            feedback += 'YELLOW'
        else:
            feedback += 'Grey'

    return feedback
attempts = 6
print(" Welcome to Wordle! Guess the 5 letter word.")

for attempt in range(attempts):
    guess = input(f"Attempt  {attempt+1}/6 - Enter a 5 letter word: ").lower()

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
