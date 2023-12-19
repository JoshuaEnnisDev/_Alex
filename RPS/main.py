import pgzrun
import random

WIDTH = 800
HEIGHT = 800


# make a list of choices
brain_choices = ["rock", "paper", "scissors"]

player_choice = ""
brain = ""
display_text = ""
player_score = 0
com_score = 0

# create actors
paper_btn = Actor("paper", (150, 200))
rock_btn = Actor("rock", (400, 200))
scissors_btn = Actor("scissors", (650, 200))


def get_winner(player_choice, brain):
    global player_score
    global com_score
    
    result = ""
    # this checks if both choices are the same
    if player_choice == brain:
        result = "Tie"
    # player choses paper
    elif player_choice == "paper":
        if brain == "rock":
            result = "You win!"
            player_score += 1
        elif brain == "scissors":
            result = "You lose!"
            com_score += 1
    # player chooses rock
    elif player_choice == "rock":
        if brain == "paper":
            result = "You lose"
            com_score += 1
        elif brain == "scissors":
            result = "You win"
            player_score += 1
    # player chooses scissors
    elif player_choice == "scissors":
        if brain == "paper":
            result = "You win"
            player_score += 1
        elif brain == "rock":
            result = "You lose"
            com_score += 1
    return result


# gets called every time update does
def draw():
    screen.clear()
    screen.draw.text("Rock paper scisors", center=(400, 50), fontsize=40, color="brown")
    screen.draw.text(f"{display_text}", center=(400, 600), fontsize=40, color="brown")
    paper_btn.draw()
    rock_btn.draw()
    scissors_btn.draw()


# gets called when we click any mouse button
def on_mouse_down(pos):
    global brain
    global player_choice
    brain = random.choice(brain_choices)
    if paper_btn.collidepoint(pos):
        player_choice = "paper"
    elif rock_btn.collidepoint(pos):
        player_choice = "rock"
    elif scissors_btn.collidepoint(pos):
        player_choice = "scissors"
    display()


def display():
    global display_text
    display_text = f'''
    Computer chooses: {brain}
    Player Chooses: {player_choice}
    
        {get_winner()}
    '''


# gets called 60 times a second
def update():
    pass

pgzrun.go()
