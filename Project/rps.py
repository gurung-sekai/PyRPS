# This code takes in user input, selects a randoma ctions for the computer, and decides the winner!

import random

# Prompts the user to enter a selection and save it to a variable for later use. 
user_actions = input("Enter a choice (rock, paper, scissors): ")

# To make the computer make it's choices 
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

# System prompt 
print(f"\nYou chose {user_actions}, computer chose {computer_action}.\n")

# To determine a winner by letting the System know which hands triumphs over the other

if user_actions == computer_action: 
    print(f"Both player selected {user_actions}. It's a draw!")
elif user_actions == "rock":
    if computer_action == "scissors": 
        print("Rock smashes scissors! You win!")
    else: 
        print("Paper covers rock! You lose!")
elif user_actions == "paper": 
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else: 
        print("Scissor cuts paper! You lose!")
elif user_actions == "scissors": 
    if computer_action == "paper": 
        print("Scissors cuts paper! You win!")
    else: 
        print("Rock smashes scissors! You lose!") 






