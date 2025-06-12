from colorama import Fore, Style, init, Back

init(autoreset=True)

word = "APPLE"


colored_word = (Back.GREEN + Fore.BLACK + f" {word[0]} " + Back.LIGHTBLACK_EX + Fore.WHITE + f" {word[1]} " + Back.YELLOW + Fore.BLACK + f" {word[2]}" + Back.LIGHTBLACK_EX+ Fore.WHITE + f" {word[3]}" + Back.LIGHTBLACK_EX+ Fore.WHITE + f" {word[4]} ")


print(colored_word)