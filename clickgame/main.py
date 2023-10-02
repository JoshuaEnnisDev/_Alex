import pgzrun

WIDTH = 800
HEIGHT = 600

# actors
tank = Actor("tank_sand")

tank2 = Actor("tank_red")
tank2.x = WIDTH - 50
tank2.y = HEIGHT - 50

tree = Actor("tree")
tree.x = 400
tree.y = 300

background = Actor("sand")


def move_tank():
    if keyboard.a:
        tank.x = tank.x - 2
        tank.angle = 180
    if keyboard.w:
        tank.y = tank.y - 2
        tank.angle = 90
    if keyboard.d:
        tank.x = tank.x + 2
        tank.angle = 0
    if keyboard.s:
        tank.y = tank.y + 2
        tank.angle = 270


def bound_actor(actor):
    # left side of screen
    if actor.left < 0:
        actor.left = 0
    # top of the screen
    if actor.y < 0:
        actor.y = 0
    # right side of screen
    if actor.x > WIDTH:
        actor.x = WIDTH
    # bottom of the screen
    if actor.y > HEIGHT:
        actor.y = HEIGHT


def move_red():
    if keyboard.left:
        tank2.x = tank2.x - 2
        tank2.angle = 180
    if keyboard.up:
        tank2.y = tank2.y - 2
        tank2.angle = 90
    if keyboard.right:
        tank2.x = tank2.x + 2
        tank2.angle = 0
    if keyboard.down:
        tank2.y = tank2.y + 2
        tank2.angle = 270


def draw():
    background.draw()
    tank.draw()
    tree.draw()
    tank2.draw()


# runs 60 times per second
def update():
    screen.clear()
    move_tank()
    move_red()
    bound_actor(tank)
    bound_actor(tank2)


# last line
pgzrun.go()
