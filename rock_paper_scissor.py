import random

choices = {"r":"🪨", "p":"🧻","s":"✂️"}
while True:
    computer_choice = random.choice(list(choices.keys()))

    player = input("Enter your choice(r/p/s) or to quit 'q':").lower()
    if player == "q":
        print("Thanks for playing! 👋")
        break

    if player not in choices:
        print("invalid choice")
        exit()

    print(f'you chose {choices[player]}')    
    print(f'computer chose {choices[computer_choice]}')

    if computer_choice == player:
        print("tie!")
    elif (computer_choice == "r" and player == "p")\
        or (computer_choice == "p" and player == "s")\
        or (computer_choice == "s" and player == "r"):
        print("you won!")
    else:
        print("you lose!")