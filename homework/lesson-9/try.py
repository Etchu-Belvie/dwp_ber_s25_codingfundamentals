

import random
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# List of 5-letter words
word_list = ['spain', 'japan', 'sudan', 'niger', 'malta', 'egypt','apple', 'grape', 'mango', 'pearl', 'stone', 'climb',
    'brave', 'flame', 'drink', 'fresh', 'video', 'wheel',
    'plane', 'fruit', 'lemon', 'poise', 'actor', 'earth',
    'house', 'field','green', 'travel']

print("Welcome to Wordle! Guess the 5-letter word")
print("You get 6 attempts!")
print("Hint!")
word = "APPLE"
colored_word = (Back.GREEN + Fore.BLACK + f" {word[0]} " + Back.LIGHTBLACK_EX + Fore.WHITE + f" {word[1]} " + Back.YELLOW + Fore.BLACK + f" {word[2]}" + Back.LIGHTBLACK_EX+ Fore.WHITE + f" {word[3]}" + Back.LIGHTBLACK_EX+ Fore.WHITE + f" {word[4]} ")
print(colored_word)
print("🟩 Right letter Right Position")
print("🟨 Right letter Wrong Position")
print("⬜ wrong letter")
print("Ready? Let's Play!")

def play_wordle():
    wordle = random.choice(word_list)
    max_attempts = 6

    for attempt in range(max_attempts):
        while True:
            guess = input(f"Attempt {attempt + 1}/{max_attempts}: ").lower()
            if len(guess) == 5 and guess.isalpha():
                break
            print(Fore.RED + "Invalid input! Enter a **five-letter word** containing only alphabets.")

        # Create feedback with background-colored boxes
        feedback = []
        for i in range(len(wordle)):
            letter = guess[i].upper()
            if guess[i] == wordle[i]:
                # Green background for correct position
                feedback.append(Back.GREEN + Fore.BLACK + f" {letter} " + Style.RESET_ALL)
            elif guess[i] in wordle:
                # Yellow background for correct letter wrong position
                feedback.append(Back.YELLOW + Fore.BLACK + f" {letter} " + Style.RESET_ALL)
            else:
                # Gray background for incorrect letter
                feedback.append(Back.LIGHTBLACK_EX + Fore.WHITE + f" {letter} " + Style.RESET_ALL)

        print("".join(feedback))  # Show feedback line

        if guess == wordle:
            print(Fore.CYAN + "\n🎉 Congratulations! You guessed the word correctly!")
            break
    else:
        print(Fore.MAGENTA + f"\n😢 Out of attempts! The correct word was '{wordle.upper()}'.")

# Start the game
play_wordle()