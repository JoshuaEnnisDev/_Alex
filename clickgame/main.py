import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "Dev"
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

# game state
start_screen = True
game_active = False
game_over = False

# start screen
tank_button = Rect(200, 300, 100, 100)
# tank_button_image = Actor("tank_sand", tank_button.center, anchor=('center', 'center'))
tank_button_image = Actor("tank_sand")
tank_button_image.x = tank_button.centerx
tank_button_image.y = tank_button.centery


tank2_button = Rect(400, 300, 100, 100, anchor=(0.5, 0.5))
tank2_button_image = Actor("tank_red", tank2_button.center)


def draw_start_screen():
    screen.draw.text("Tanks!", fontsize=50, centerx=WIDTH / 2, centery=100)
    screen.draw.text(
        "Choose your character",
        centerx=WIDTH / 2,
        centery=200,
        fontsize=40,
        shadow=(0.5, 0.5),
        scolor="blue",
        angle=25
        )

    screen.draw.filled_rect(tank_button, "green")
    tank_button_image.draw()
    screen.draw.filled_rect(tank2_button, "green")
    tank2_button_image.draw()


def choose_character(pos):
    global start_screen
    global game_active
    if tank_button.collidepoint(pos):
        tank.image = "tank_sand"
        start_screen = False
        game_active = True
    if tank2_button.collidepoint(pos):
        tank.image = "tank_red"
        start_screen = False
        game_active = True


def draw_button(image, color, rect):
    screen.draw.filled_rect(rect, color)
    screen.blit(image, rect.center)


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


def bullet_left_screen():
    for bullet in bullets:
        # checks if bullet is off the screen
        if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
            # bullets.remove(bullet)
            return True


def get_bullet():
    for bullet in bullets:
        if bullet_left_screen():
            return bullet
        if bullet.colliderect(tank2):
            tank2.hit = True
            return bullet


def remove_bullet():
    if not get_bullet() is None:
        bullets.remove(get_bullet())
        

def collide_tank():
    if tank.colliderect(tank2):
        tank2.hit = True
        tank.hit = True


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


def on_mouse_down(pos):
    global start_screen
    global game_active
    if start_screen:
        choose_character(pos)


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
    if game_active:
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
    elif start_screen:
        draw_start_screen()
    else:
        pass


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
    collide_tank()
    explode(tank2)
    

# last line
pgzrun.go()
