import random

choices = {"r":"🪨", "p":"🧻","s":"✂️"}

def get_user_choice():
    while True:
        player = input("Enter your choice(r/p/s) or to quit 'q':").lower()
        if player == "q":
            print("Thanks for playing! 👋")
            exit()
        elif player not in choices:
            print("invalid choice")
        else:
            return player
def determine_winner(computer_choice,player):
    if computer_choice == player:
        print("tie!")
    elif (computer_choice == "r" and player == "p")\
        or (computer_choice == "p" and player == "s")\
        or (computer_choice == "s" and player == "r"):
        print("you won!")
    else:
        print("you lose!")

def play_game():
    while True:
        computer_choice = random.choice(list(choices.keys()))
        player = get_user_choice()

        print(f'you chose {choices[player]}')    
        print(f'computer chose {choices[computer_choice]}')
        
        determine_winner(computer_choice,player)

play_game()
