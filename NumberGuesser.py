# ╔═══════════════════════════════════►
# ║   Made by sava4ka.
# ║   11/8/2021
# ║   Time spent: 2 hours
# ║   It's my firs time trying Python.
# ║   If you use it somewhere, credit the author.
# ║
# ║
# ║  Github: https://github.com/sava4ka777/NumberGuesser
# ║
# ║  Luv u :3
# ║ ║▌│█│║▌║█║│║▌║
# ║ ║▌│█│║▌║█║│║▌║
# ║ ║▌│█│║▌║█║│║▌║
# ╚═══════════════════════════════════►

from colorama import init
init()
from colorama import Fore, Back, Style
import random

#Prints the logo
print (Fore.CYAN + "███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░  ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗███████╗██████╗░")
print (Fore.CYAN + "████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗  ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗")
print (Fore.CYAN + "██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝  ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░█████╗░░██████╔╝")
print (Fore.CYAN + "██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗  ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██╔══██╗")
print (Fore.CYAN + "██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║  ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝███████╗██║░░██║")
print (Fore.CYAN + "                                                                                         Made by sava4ka         ")
#Line skip
print (" ")
#Rules
print (Fore.GREEN + "Rules are simple: Computer generates a number, you have to guess it.")
print(" ")
input(Fore.WHITE + "Press enter to continue.")

#Line skip
print (" ")
#Difficulty
print(Fore.MAGENTA + "Choose difficulty:")
print(Fore.GREEN + "1.Easy(1-5)")
print(Fore.YELLOW + "2.Normal(1-10)")
print(Fore.RED + "3.Hard(1-35)")
#Line skip
print (" ")
#Difficulty choosing
difficulty = input(Fore.WHITE + "Enter difficulty number: ")

if difficulty == str(1):
 random_number = str(random.randint(1,5))
elif difficulty == str(2):
  random_number = str(random.randint(1,10))
elif difficulty == str(3):
     random_number = str(random.randint(1,35))
else:
        print(Fore.RED + "Invalid difficulty number, restart and please enter the number from 1 to 3.")
#Number choosing
print (Fore.YELLOW + "Generating number...")
print (Fore.YELLOW + "Done.")
user_number = input (Fore.GREEN + "Enter your number: ")
if user_number == random_number:
    print (Fore.CYAN + "You're right! The number was " + user_number)
if user_number != random_number:
    print(Fore.RED + "You're wrong, the number was " + random_number)
