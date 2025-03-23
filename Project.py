from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_jump):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.jump = player_jump
        self.vel_y = 0
        self.on_ground = False

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_jump):
        super().__init__(player_image, player_x, player_y, player_speed, player_jump)
        self.vel_y = 0
        self.on_ground = False
        self.jump_count = 0
        self.jump_cooldown = 0

    def update(self):
        keys = key.get_pressed()
        dx = 0
        dy = 0

        if keys[K_LEFT] and self.rect.x > 5:
            dx = -self.speed
        if keys[K_RIGHT] and self.rect.x < 750:
            dx = self.speed

        # Лестницы
        ladder_collision = sprite.spritecollideany(self, leders)
        if ladder_collision:
            if keys[K_UP]:
                dy = -self.speed
            if keys[K_DOWN]:
                dy = self.speed
            self.vel_y = 0  # отключить гравитацию на лестнице

        #прыжок
        if keys[K_UP] and self.jump_cooldown == 0 and not ladder_collision:
            if self.on_ground:
                self.vel_y = -15
                self.jump_count = 1
                self.jump_cooldown = 10
            elif self.jump_count == 1:
                self.vel_y = -15
                self.jump_count = 2
                self.jump_cooldown = 10

        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1

        # Гравитация
        if not ladder_collision:
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

        # Коллизии
        self.on_ground = False
        self.rect.x += dx
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if dx > 0:
                    self.rect.right = platform.rect.left
                if dx < 0:
                    self.rect.left = platform.rect.right

        self.rect.y += dy
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                    self.jump_count = 0
                elif self.vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
    def fire(self):
        bullet = Bullet("fireball.png", self.rect.x + 15, self.rect.y, 30, 0)
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.x += 20
        if self.rect.y<0:
            self.kill()

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 454:
            self.direction = "right"
        if self.rect.x >= 743:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update1(self):
        if self.rect.x <= 600:
            self.direction = "right"
        if self.rect.x >= 730:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Portal(GameSprite):
    def update(self):
        self.speed = 0

window = display.set_mode((800, 600))
display.set_caption("Магічний котел")
background = transform.scale(image.load("background.png"), (800, 600))

level = [
   "                " ,
   "              +u",
   "            ----",
   "                ",
   "    8           ",
   "  + H           ",
   "  - H        +  ",
   "+   H    +  H-- ",
   "--      --  H   ",
   "    ---     H   ",
   "+        +      ",
   "----------------"]

platforms = sprite.Group()
coldrons = sprite.Group()
leders = sprite.Group()
glasses = sprite.Group()
clevers = sprite.Group()
portals = sprite.Group()
magician = Player("magician.png", 50, 500, 10, 30)
enemy = Enemy("enemy.png", 725, 486, 5, 0)
enemy1 = Enemy("enemy.png", 743, 286, 5, 0)
bullets = sprite.Group()
portal1 = Portal("portal.png",756,483,0,0 )
x = 0
y = 0
for plt in level:
    x = 0
    for p in plt:
        if p == "-":
            platform = GameSprite('grass.png', x, y, 0, 0)
            platforms.add(platform)
        if p == "0":
            portal = GameSprite('portal.png', x, y, 0, 0)
            portals.add(portal)
        if p == "u":
            coldron = GameSprite('coldrone.png', x, y, 0, 0)
            coldrons.add(coldron)
        if p == "H":
            leder = GameSprite('ladder.png', x, y, 0, 0)
            leders.add(leder)
        if p == "8":
            glass = GameSprite('glass.png', x, y, 0, 0)
            glasses.add(glass)
        if p == "+":
            clever = GameSprite('clever.png', x, y, 0, 0)
            clevers.add(clever)
        x += 50
    y += 50

kaunt = 0
game = True
clock = time.Clock()
FPS = 120

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

text = font.render("" + str(kaunt), 1, (255, 255, 255))
window.blit(text, (10, 20))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                magician.fire()

    magician.update()

    window.blit(background, (0, 0))
    magician.reset()
    enemy.reset()
    enemy.update()
    enemy1.reset()
    enemy1.update1()
    bullets.draw(window)
    bullets.update()
    portal1.update()
    portal1.reset()

    for platform in platforms:
        platform.reset()
    for coldron in coldrons:
        coldron.reset()
    for leder in leders:
        leder.reset()
    for glass in glasses:
        glass.reset()
    for clever in clevers:
        clever.reset()
    if sprite.collide_rect(magician, enemy):
        window.blit(lose, (200, 200))
        magician.rect.x = 50
        magician.rect.y = 500
        finish = True
    if sprite.collide_rect(magician, enemy1):
        window.blit(lose, (200, 200))
        magician.rect.x = 50
        magician.rect.y = 500
        finish = True
    if sprite.collide_rect(magician, portal1):
        magician.rect.x = 50
        magician.rect.y = 650


    display.update()
    time.delay(50)
    clock.tick(FPS)
