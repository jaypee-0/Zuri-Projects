import random

print("Enter a choice:")
while True:
    user_action = input("rock, paper, scissors: ")

    actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action.lower() == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action.lower() == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action.lower() == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    playAgain = input("Play again? (y/n): ")
    if playAgain.lower() != "y":
        break