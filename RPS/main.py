import pgzrun
import random

WIDTH = 800
HEIGHT = 800



#global variables

# make a list of choices
brain_choices = ["rock", "paper", "scissors"]
# get a random selection
brain = random.choice(brain_choices)
player_choice = ""
display_text = ""

# create actors
paper_btn = Actor("paper", (150, 200))
rock_btn = Actor("rock", (400, 200))
scissors_btn = Actor("scissors", (650, 200))


def game_play():
    global display_text
    display_text = ""
        
    # this checks if both choices are the same
    if player_choice == brain:
        display_text = "Tie"
    # player choses paper
    elif player_choice == "paper":
        if brain == "rock":
            display_text = "You win!"
        elif brain == "scissors":
            display_text = "You lose!"
    # player chooses rock
    elif player_choice == "rock":
        if brain == "paper":
            display_text = "You lose"
        elif brain == "scissors":
            display_text = "You win"
    # player chooses scissors
    elif player_choice == "scissors":
        if brain == "paper":
            display_text = "You win"
        elif brain == "scissors":
            display_text = "You lose"
        

# gets called every time update does
def draw():
    screen.draw.text("Rock paper scisors", center=(400, 50), fontsize=40, color="brown")
    screen.draw.text(f"{display_text}", center=(400, 600), fontsize=40, color="brown")
    paper_btn.draw()
    rock_btn.draw()
    scissors_btn.draw()


# gets called when we click any mouse button
def on_mouse_down(pos):
    global player_choice
    if paper_btn.collidepoint(pos):
        player_choice = "paper"
    elif rock_btn.collidepoint(pos):
        player_choice = "rock"
    elif scissors_btn.collidepoint(pos):
        player_choice = "scissors"
    game_play()


# gets called 60 times a second
def update():
    pass


pgzrun.go()
