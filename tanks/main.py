import pgzrun

WIDTH = 800
HEIGHT = 600

# empty list
bullets = []
bullet_speed = 5

# actors
tank = Actor("tank_sand")
tank.is_exploding = False
tank.is_dead = False

tank2 = Actor("tank_red")
tank2.x = WIDTH - 50
tank2.y = HEIGHT - 50
tank2.is_exploding = False
tank2.is_dead = False

tree = Actor("tree")
tree.x = 400
tree.y = 300

background = Actor("sand")

explosions = ["explosion1", "explosion2", "explosion3", "explosion4", "explosion5"]
timer = 15
index = 0
select_screen = True


def explode(actor):
    global timer
    global index
    if actor.is_exploding:
        actor.image = explosions[index]
        timer = timer - 1
        if timer <= 0:
            timer = 15
            if index == len(explosions) - 1:
                # actor.pos = (-100, -100)
                actor.is_exploding = False
                actor.is_dead = True
            index = index + 1


def check_dead(actor):
    if actor.is_dead:
        actor.pos = (-100, -100)


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
            tank2.is_exploding = True


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


def collision():
    if tank.colliderect(tank2):
        tank.is_exploding = True


# this function is called when a key is pressed
def on_key_down():
    if keyboard.f and not tank.is_exploding:
        # create the bullet actor
        bullet = Actor("bullet_blue")
        # set the bullet's position and angle
        bullet.x = tank.x
        bullet.y = tank.y
        bullet.angle = tank.angle
        # add it to the list
        bullets.append(bullet)


button1 = Rect(200, 150, 100, 100)
button1_image = Actor("tank_sand", button1.center)


def on_mouse_down(pos):
    global select_screen
    if button1.collidepoint(pos):
        select_screen = False


def draw():
    # select screen
    global select_screen
    if select_screen:
        screen.fill("#e69d29")
        screen.draw.text("Tanks", center=(WIDTH / 2, 50), fontsize=50)
        screen.draw.filled_rect(button1, "#15701d")
        button1_image.draw()
    # main game
    elif not tank.is_dead and not tank2.is_dead:
        background.draw()
        tree.draw()

        if not tank2.is_dead:
            tank2.draw()
        else:
            tank2.pos = (-100, -100)
        
        if not tank.is_dead:
            tank.draw()
        else:
            tank.pos = (-200, -200)

        # draw all the bullets in the bullets list
        for bullet in bullets:
            bullet.draw()
    # game over screen
    else:
        screen.clear()
        screen.draw.text("Game over!", (0, 0), fontsize=100)


# runs 60 times per second
def update():
    screen.clear()
    move_tank()
    move_red()
    bound_actor(tank)
    bound_actor(tank2)
    move_bullet()
    remove_bullet()
    collision()
    explode(tank2)
    explode(tank)
    check_dead(tank)
    check_dead(tank2)


# last line
pgzrun.go()
