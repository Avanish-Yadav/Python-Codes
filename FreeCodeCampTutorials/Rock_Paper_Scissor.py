import random
def get_choices():
    player_choice=input("Enter the choice(rock, paper, scissor)")
    computer_choice="paper"
    choices={"player":player_choice,"Computer":computer_choice}
    return choices

choices=get_choices()
print(choices)