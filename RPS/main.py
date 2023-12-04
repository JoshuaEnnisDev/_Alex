import pgzrun
import random

WIDTH = 800
HEIGHT = 800

# get a random selection

# make a list of choices
brain_choices = ["rock", "paper", "scissors"]
brain = random.choice(brain_choices)
player_choice = ""  


paper_btn = Actor("paper", (150, 200))
rock_btn = Actor("rock", (400, 200))
scissors_btn = Actor("scissors", (650, 200))


def draw():
    paper_btn.draw()
    rock_btn.draw()
    scissors_btn.draw()


def on_mouse_down(pos):
    global player_choice
    if paper_btn.collidepoint(pos):
        player_choice = "paper"
    elif rock_btn.collidepoint(pos):
        player_choice = "rock"
    elif scissors_btn.collidepoint(pos):
        player_choice = "scissors"


pgzrun.go()