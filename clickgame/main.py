import pgzrun

WIDTH = 800
HEIGHT = 600

# actors
tank = Actor("tank_sand")
tree = Actor("tree")
background = Actor("sand")


def draw():
    background.draw()
    tank.draw()
    tree.draw()


# runs 60 times per second
def update():
    screen.clear()
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


# last line
pgzrun.go()
