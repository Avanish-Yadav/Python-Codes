import random
def get_choices():
    player_choice=input("Enter the choice(rock, paper, scissor)- ")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print("You choose "+player+" Computer choice "+computer)
    if player==computer:
        return "Its the tie!"
    elif player=="rock":
        if computer=="scissors":
            return "Rock smashes scissors! You win !"
        else:
            return "Paper covers rock! You lose"
    elif player==computer:
        return "Its the tie!"
    elif player=="scissors":
        if computer=="paper":
            return "Scissors cuts paper! You win !"
        else:
            return "Rock smashes scissors! You lose"


choices=get_choices()
result=check_win(choices["player"],choices["computer"])
print(result)


""""
choices={"player":"rock","computer":"paper"}
p_choice=choices["player"]
c_choice=choices["computer"]
"""
"""
    age=25
    print(f"Jim is  {age} years old")--This also the way to print string & number together
"""

