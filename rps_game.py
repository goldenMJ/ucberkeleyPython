# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computerChoice = random.choice(options)

# User Selection
kadar_choice = input()

# Run Conditionals

if (user == "r" and computerChoice == "p"):
    print("sorry, Kadar. You lose, paper over rock")

elif (user == "r" and computerChoice == "s"):
    print("yeah, Kadar. You won, rock over scissors! Computers are dumb!")
    
elif (user == "r" and computerChoice == "r"):
    print("TIE, Kadar! You both chose rock, sorry girl!")

elif (user == "r" and computerChoice == "p"):
    print("sorry, Kadar. You lose, paper over rock")

elif (user == "p" and computerChoice == "p"):
    print("TIE, Kadar! You both chose paper, sorry girl!")

elif (user == "p" and computerChoice == "s"):
    print("oh nooo, Kadar. Scissors win! Sorry, not sorry!")
    
elif (user == "s" and computerChoice == "r"):
    print("Neinnn!Stein gewinnt!")

elif (user == "r" and computerChoice == "p"):
    print("sorry, Kadar. You lose, paper over rock")
    
elif (user == "r" and computerChoice == "r"):
    print("TIE, Kadar! You both chose rock, sorry girl!")
