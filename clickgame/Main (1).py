import pgzrun
WIDTH = 800
HEIGHT = 600
bullets = []
bullet_speed = 10
#actors
tank = Actor("tank_sand")
meteor = Actor ('tank_red')
meteor.x = WIDTH - 50
meteor.y = HEIGHT - 50
meteor.is_exploding = False
meteor.is_dead = False
tank.is_exploding = False
tank.is_dead = False
water = Actor("sand")
button1 = Rect(200, 150, 125, 100)
button1_image = Actor("tank_sand", button1.center)
button2 = Rect(400, 150, 125, 100)
button2_image = Actor("tank_red", button2.center)
def check_dead(actor):
    if actor.is_dead:
        actor.pos = (-100,-100)
def collision():
    if tank.colliderect(meteor):
        tank.is_exploding = True
def on_key_down():
    if keyboard.f and not tank.is_exploding:
        bullet = Actor('bullet_blue')
        bullet.y = tank.y
        bullet.x = tank.x
        bullet.angle = tank.angle
        bullets.append(bullet)
explosions = ["explosion1","explosion2","explosion3","explosion4"]
select_screen = True
timer = 15
index = 0

def on_mouse_down(pos):
    global select_screen
    if button1.collidepoint(pos):
        select_screen = False
        tank.image = ("tank_sand")
    if button2.collidepoint(pos):
        tank.image = ("tank_red")
        select_screen = False

def explode(actor):
    global timer
    global index
    if actor.is_exploding and not actor.is_dead:
        actor.image = explosions[index]
        timer = timer - 1
        if timer <= 0:
            timer = 15
            if index == len(explosions) - 1:
                actor.is_exploding = False
                actor.is_dead = True
            index = index + 1
def draw():
    global select_screen
    if select_screen:
        screen.fill("yellow")
        screen.draw.text("TANKS AND METEORS", center=(WIDTH / 2,50), fontsize=50)
        screen.draw.filled_rect(button1, "#ffe48a")
        screen.draw.filled_rect(button2, "red")
        button2_image.draw()
        button1_image.draw()
    elif not tank.is_dead and not meteor.is_dead:
        water.draw()
        if not meteor.is_dead:
            meteor.draw()
        else:
            meteor.pos = (-488,-488)
        if not tank.is_dead:
            tank.draw()
        else:
            tank.pos = (-500,-500)
        for bullet in bullets:
            bullet.draw()
    else:
        screen.clear()
        screen.draw.text("GAME OVER!", (200,300), fontsize = 100)
def move_bullet():
    for bullet in bullets:
        #right
        if bullet.angle == 0:
            bullet.x += bullet_speed
            #up
        if bullet.angle == 90:
            bullet.y -= bullet_speed
            #left
        if bullet.angle == 180:
            bullet.x -= bullet_speed
            #down
        if bullet.angle == 270:
            bullet.y += bullet_speed
def bound_actor(actor):
    if actor.x < 0:
        actor.x = 0
    if actor.y < 0:
        actor.y = 0
    if actor.x > WIDTH:
        actor.x = WIDTH
    if actor.y > HEIGHT:
        actor.y = HEIGHT
def remove_bullets():
    for bullet in bullets:
        if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
            bullets.remove(bullet)
        if bullet.colliderect(meteor):
            bullets.remove(bullet)
            meteor.is_exploding = True
def move_meteor():
    if keyboard.a:
        meteor.angle = 180
        meteor.x = meteor.x - 1
    if keyboard.d:
        print("Debug")
        meteor.angle = 0
        meteor.x = meteor.x + 1
    if keyboard.w:
        meteor.angle = 90
        meteor.y = meteor.y - 1
    if keyboard.s:
        meteor.angle = 270
        meteor.y = meteor.y + 1
def move_tank():
    if keyboard.left:
        tank.angle = 180
        tank.x = tank.x - 1
    if keyboard.right:
        tank.angle = 0
        tank.x = tank.x + 1
    if keyboard.down:
        tank.angle = 270
        tank.y = tank.y + 1
    if keyboard.up:
        tank.angle = 90
        tank.y = tank.y - 1
def update():
    screen.clear()
    
    move_tank()
    move_bullet()
    bound_actor(meteor)
    bound_actor(tank)
    remove_bullets()
    collision()
    explode(meteor)
    explode(tank)
    check_dead(tank)
    check_dead(meteor)
    move_meteor()
pgzrun.go()