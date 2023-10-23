import pgzrun

WIDTH = 800
HEIGHT = 600

# empty list
bullets = []
bullet_speed = 5

# actors
tank = Actor("tank_sand")

tank2 = Actor("tank_red")
tank2.x = WIDTH - 50
tank2.y = HEIGHT - 50
tank2.timer = 60
tank2.hit = False
tank2.dead = False

tree = Actor("tree")
tree.x = 400
tree.y = 300

background = Actor("sand")

explosions = ["explosion1", "explosion2", "explosion3", "explosion4", "explosion5"]
timer = 20
index = 0


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


def remove_bullet():

    for bullet in bullets:
        # checks if bullet is off the screen
        if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
            bullets.remove(bullet)
        # checks collision with the other player
        if bullet.colliderect(tank2):
            bullets.remove(bullet)
            tank2.hit = True


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


def move_bullet():
    for bullet in bullets:
        # right
        if bullet.angle == 0:
            bullet.x += bullet_speed
        # up
        if bullet.angle == 90:
            bullet.y -= bullet_speed
        # left
        if bullet.angle == 180:
            bullet.x -= bullet_speed
        # down
        if bullet.angle == 270:
            bullet.y += bullet_speed


# this function is called when a key is pressed
def on_key_down():
    print(bullets)
    if keyboard.f:
        # create the bullet actor
        bullet = Actor("bullet_blue")
        # set the bullet's position and angle
        bullet.x = tank.x
        bullet.y = tank.y
        bullet.angle = tank.angle
        # add it to the list
        bullets.append(bullet)


def draw():
    background.draw()
    tank.draw()
    tree.draw()
    if not tank2.dead:
        tank2.draw()
    else:
        tank2.pos = (-100, -100)

    # draw all the bullets in the bullets list
    for bullet in bullets:
        bullet.draw()


def explode(actor):
    global timer
    global index
    if actor.hit:
        actor.image = explosions[index]
        timer -= 1
        if timer <= 0:
            timer = 10
            if index == len(explosions) - 1:
                actor.hit = False
                actor.dead = True
            index += 1


# runs 60 times per second
def update():
    screen.clear()
    move_tank()
    move_red()
    bound_actor(tank)
    bound_actor(tank2)
    move_bullet()
    remove_bullet()
    explode(tank2)

# last line
pgzrun.go()
