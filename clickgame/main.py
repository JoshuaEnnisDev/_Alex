import pgzrun

WIDTH = 800
HEIGHT = 600

test_rect = Rect(20, 20, 100, 100)
sandbag = Actor("tank_red")


def draw():
    screen.clear()
    sandbag.draw()
    screen.draw.filled_rect(test_rect, "green")


def update():
    # test_rect.x = test_rect.x + 2
    sandbag.x = sandbag.x + 2


# last line
pgzrun.go()
