import random
user_choice = input(" Enter your choice (rock, paper, or scissors): ").lower()

possible_choices = ["rock" , "paper" , "scissors"]
ai_choice = random.choice(possible_choices)

if user_choice  == ai_choice:
    print( "It's a tie!")
elif user_choice == "rock":
    if ai_choice == "scissors":
        print("Rock beats scissors. You win!")
    else:
        print("Paper beats rock. You lose.")
elif user_choice == "paper":
    if ai_choice == "rock":
        print("Paper beats rock. You win!")
    else:
        print("Scissors beats paper. You lose.")
elif user_choice == "scissors":
    if ai_choice == "paper":
        print("Scissors beats paper. You win!")
    else:
        print("Rock beats scissors. You lose.")
