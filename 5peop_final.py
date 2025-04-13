from pygame import * 
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_jump):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 60))
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
            self.image=transform.scale(image.load("magician_l.png"), (60, 60))
        if keys[K_RIGHT] and self.rect.x < 750:
            dx = self.speed
            self.image=transform.scale(image.load("magician_r.png"), (60, 60))

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
        fire_sound.play()
        

class Bullet(GameSprite):
    def update(self):
        self.rect.x += 10
        if self.rect.y<0:
            self.kill()
class EnemyBullet(GameSprite):
    def update(self):
        self.rect.x -= 10
        if self.rect.y<0:
            self.kill()

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 454:
            self.direction = "right"
            self.image=transform.scale(image.load("Enemy_r.png"), (60, 60))
        if self.rect.x >= 743:
            self.direction = "left"
            self.image=transform.scale(image.load("Enemy_l.png"), (60, 60))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update1(self):
        if self.rect.x <= 600:
            self.direction = "right"
            self.image=transform.scale(image.load("Enemy_r.png"), (60, 60))
        if self.rect.x >= 730:
            self.direction = "left"
            self.image=transform.scale(image.load("Enemy_l.png"), (60,60))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update2(self):
        if self.rect.x <= 150:
            self.direction = "right"
            self.image=transform.scale(image.load("Enemy_r.png"), (60, 60))
        if self.rect.x >= 310:
            self.direction = "left"
            self.image=transform.scale(image.load("Enemy_l.png"), (60,60))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update3(self):
        if self.rect.x <= 410:
            self.direction = "right"
            self.image=transform.scale(image.load("Enemy_r.png"), (60, 60))
        if self.rect.x >= 600:
            self.direction = "left"
            self.image=transform.scale(image.load("Enemy_l.png"), (60,60))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update4(self):
        if self.rect.x <= 20:
            self.direction = "right"
            self.image=transform.scale(image.load("Enemie_r.png"), (60, 60))
        if self.rect.x >= 600:
            self.direction = "left"
            self.image=transform.scale(image.load("Enemie_l.png"), (60,60))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


    def fire(self):
        bullet1 = EnemyBullet("shadowball.png", self.rect.x + 15, self.rect.y, 30, 0)
        bullets1.add(bullet1)
        fire_sound.play()

class BossBullet(GameSprite):
    def update(self):
        self.rect.y += randint(3,6)
        if self.rect.y > 600: 
            self.kill()

class Boss(sprite.Sprite):
    def __init__(self, boss_image, boss_x, boss_y):
        super().__init__()
        self.image = transform.scale(image.load(boss_image), (236, 236))
        self.rect = self.image.get_rect()
        self.rect.x = boss_x
        self.rect.y = boss_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def fire(self):
        for i in range(randint(7,10)):
            bullet2 = BossBullet("sakuraball.png", randint(1,600), 50, randint(5,10), 0)
            bullets2.add(bullet2)
            fire_sound.play()
    def fire1(self):
            bullet3 = EnemyBullet("sakuraball1.png", self.rect.x + 15, 450, 30, 0)
            bullets3.add(bullet3)
            fire_sound.play()



class Portal(GameSprite):
    def update(self):
        self.speed = 0


class Button():
    def __init__(self, color, x, y, w, h, text, fsize, txt_color):

        self.width = w
        self.height = h
        self.color = color

        self.image = Surface([self.width, self.height])
        self.image.fill((color))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.fsize = fsize
        self.text = text
        self.txt_color = txt_color
        self.txt_image = font.Font(None, fsize).render(text, True, txt_color)
    def draw(self, shift_x, shift_y): # цей метод малює кнопку із тектом в середині. Сам текст зміщенний на величини shift_x та shift_y
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.txt_image, (self.rect.x + shift_x, self.rect.y + shift_y))   
mixer.init()         
font.init()
window=display.set_mode((800,600))
display.set_caption("Магічний котел")
background=transform.scale(image.load("menu.png"),(800,600))
btn_start = Button((66, 49, 133, 1), 278, 310, 232, 69, 'START GAME',50, (255, 255, 255))
btn_end = Button((66, 49, 133, 1), 278, 487, 232, 69,'CLOSE' ,50, (255,255,255))
btn_info = Button((66, 49, 133, 1), 278, 399, 232, 69, 'CONTROL', 50, (255,255,255))
btn_menu = Button((255, 29, 109, 10), 260, 350, 280, 70, 'MENU',50, (255, 255, 255))
btn_end1 = Button((0, 180, 0, 0), 260, 445, 280, 70,'CLOSE' ,50, (255,255,255))
btn_restart = Button((255, 29, 109, 10), 260, 445, 280, 70,'RESTART' ,50, (255,255,255))
info1 = Button((66, 49, 133, 1), 50, 100, 700, 50, "Стрілка вправо - герой йде на право", 30, (255, 255, 255))
info2 = Button((66, 49, 133, 1), 50, 150, 700, 50, "Стрілка вліво - герой йде на ліво", 30, (255, 255, 255))
info3 = Button((66, 49, 133, 1), 50, 200, 700, 50, "Стрілка вгору - герой стрибае, в героя є 2 стрибки", 27, (255, 255, 255))
info4 = Button((66, 49, 133, 1), 50, 250, 700, 50, "Калвіша 'Space' - герой стріляє", 30, (255, 255, 255),)
info5 = Button((66, 49, 133, 1), 50, 300, 700, 50, "Калвіша 'E' - перехід на наступний рівень", 30, (255, 255, 255),)
info6 = Button((66, 49, 133, 1), 50, 350, 700, 50, "", 30, (255, 255, 255),)
info7 = Button((66, 49, 133, 1), 50, 400, 700, 50, "Для переходу на насупний рівень збери всі", 30, (255, 255, 255),)
info8 = Button((66, 49, 133, 1), 50, 450, 700, 50, "інгредієнти та натисни на клавішу для переходу.", 27, (255, 255, 255),)
btn_back = Button((66, 49, 133, 1), 50, 25, 100, 50, "Back", 30, (255, 255, 255),)
def inf():
    global menu,game,info
    window=display.set_mode((800,600))
    display.set_caption("Інформація")
    background1=transform.scale(image.load("information.png"),(800,600))
    info=True
    FPS=120
    clock = time.Clock()
    
    menu = False
    while info:
        for e in event.get():
            if e.type == QUIT:
                game = False
                info = False
        window.blit(background1,(0,0))
        info1.draw(15,5)
        info2.draw(15,5)
        info3.draw(15,5)
        info4.draw(15,5)
        info5.draw(15,5)
        info6.draw(15,5)
        info7.draw(15,5)
        info8.draw(15,5)
        btn_back.draw(15,5)

        pos_x, pos_y = mouse.get_pos()
        for e in event.get():
            if btn_back.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                menu = True
                info = False
                game = False
        display.update()
        time.delay(50)
        clock.tick(FPS)
kill = False
menu = True
game = False
win = False
mixer.music.load('MenuSound.ogg')
mixer.music.play()
while menu:
    for e in event.get():
        if e.type==QUIT:
            menu=False
    window.blit(background,(0,0))
    btn_start.draw(15,5)
    btn_end.draw(15,5)
    btn_info.draw(15,5)
    display.update()
    time.delay(50)
    pos_x, pos_y = mouse.get_pos()
    for e in event.get():
        if btn_start.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
            menu = False
            game = True
            kill = False
        if btn_info.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
            menu = False
            game = False
            kill = False
            info = True
            inf()
        if btn_end.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
            menu = False
            game = False
            kill = False
            win = False
window = display.set_mode((800, 600))
display.set_caption("Магічний котел")
background = transform.scale(image.load("background.jpg"), (800, 600))



level = [
   "                " ,
   "              +u",
   "            ----",
   "                ",
   "    8     -     ",
   "  + H-          ",
   "  - H        +  ",
   "+   H    +  H-- ",
   "--      --  H   ",
   "    ---     H   ",
   "+        +   +  ",
   "----------------"]

platforms = sprite.Group()
coldrons = sprite.Group()
leders = sprite.Group()
glasses = sprite.Group()
clevers = sprite.Group()
magician = Player("magician.png", 50, 500, 5, 15)
enemy = Enemy("enemy.png", 725, 486, 2, 0)
enemy1 = Enemy("enemy.png", 743, 286, 2, 0)
enemy2 = Enemy("enemy.png", 150, 245, 2, 0)
enemy3 = Enemy("enemy.png", 560, 200, 2, 0)
enemy4 = Enemy("enemy.png", 203, 54, 0,0)
enemy5 = Enemy("Enemie.png", 510, 486, 1,0)
enemy6 = Enemy("Enemie.png", 550, 486, 1,0)
enemy7 = Enemy("Enemie.png", 600, 486, 1,0)
boss = Boss("ghost.png",564,310)
enemys=sprite.Group()
enemys.add(enemy)
enemys.add(enemy1)
enemys.add(enemy3)
enemys.add(enemy2)
enemys.add(enemy4)
enemys.add(boss)
enemys.add(enemy5)
enemys.add(enemy6)
enemys.add(enemy7)



level_potion = GameSprite("level_potion.png", 750,30,0,0)
bullets = sprite.Group()
bullets1 = sprite.Group()
bullets2 = sprite.Group()
bullets3 = sprite.Group()
Icon = GameSprite("Icon.png", 0, 0, 0, 0)
icon_clever = GameSprite("clever1.png", 0, 80, 0, 0)
icon_glass = GameSprite("glass1.png", 0, 110, 0, 0)

x = 0
y = 0

for plt in level:
    x = 0
    for p in plt:
        if p == "-":
            platform = GameSprite('grass.png', x, y, 0, 0)
            platforms.add(platform)

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

level2 = [
   "                ",
   "    u0H         ",
   "    --H         ",
   "      H      0  ",
   "      H     H-- ",
   "      0     H   ",
   "   -H--  8  H   ",
   "    H   -----   ",
   "    H           ",
   "    H           ",
   "0           0   ",
   "----------------"]

cristals = sprite.Group()


level2_active = False
def start_level2():
    global level2_active
    level2_active = True

clock = time.Clock()
FPS = 45
HIT_COOLDOWN = 600  # кулдаун в миллисекундах
last_hit_time = 0
Stamina_Cooldown = 0
Enemy_StaminaCooldown = 0
BossStamina_Cooldown = 0
last_stamina_time = 0

font = font.Font(None, 40)



def level_2():
    global level2_active  
    start_level2()
    reset_level1()  
    magician.rect.x = 50  
    magician.rect.y = 400
    x = 0
    y = 0
    for plt in level2:
        x = 0
        for p in plt:
            if p == "-":
                platform = GameSprite('grass2.png', x, y, 0, 0)
                platforms.add(platform)

            if p == "u":
                coldron = GameSprite('coldrone.png', x, y, 0, 0)
                coldrons.add(coldron)
            if p == "H":
                leder = GameSprite('ladder.png', x, y, 0, 0)
                leders.add(leder)
            if p == "8":
                glass = GameSprite('glass.png', x, y, 0, 0)
                glasses.add(glass)
            if p == "0":
                cristal = GameSprite('cristal.png', x, y, 0, 0)
                cristals.add(cristal)
            x += 50
        y += 50


def reset_level1():
    platforms.empty()
    coldrons.empty()
    leders.empty()
    glasses.empty()
    clevers.empty()
    enemy1.rect.y = -150
    enemy.rect.y = -150

def reset_level2():
    platforms.empty()
    coldrons.empty()
    leders.empty()
    glasses.empty()
    cristals.empty()
    enemy2.rect.y = -150
    enemy3.rect.y = -150
    enemy4.rect.y = -150

fire_sound=mixer.Sound('FireSound.ogg')
kill_sound=mixer.Sound('KillSound.ogg')
mixer.music.load('PlaySound.ogg')
mixer.music.play()
colletction = 0
colletction1 = 0
colletction2 = 0
colletction3 = 0
colletction4 = 0
#Health of magician
magician_health = 3
#Health of enemy
enemy_health = 2
#Health of enemy1
enemy1_health = 2
enemy2_health = 2
enemy3_health = 2
enemy4_health = 5
#Stamina of magician
magician_stamina = 3
enemy4_stamina = 1
#Health of Boss
boss_health = 50
boss_stamina = 1
enemy5_health = 0
enemy6_health = 0
enemy7_health = 0

level2_enemies = 1
level_potion1_collected = False

level3 = [
   "                ",
   "                ",
   "                ",
   "                ",
   "                ",
   "                ",
   "                ",
   "                ",
   "                ",
   "                ",
   "                ",
   "----------------"]

level3_active = False
def start_level3():
    global level3_active
    level3_active = True

def level_3():
    global level3_active  
    start_level3()
    reset_level2()  
    magician.rect.x = 50  
    magician.rect.y = 400
    x = 0
    y = 0
    for plt in level3:
        x = 0
        for p in plt:
            if p == "-":
                platform = GameSprite('grass3.png', x, y, 0, 0)
                platforms.add(platform)
            x += 50
        y += 50

background2 = transform.scale(image.load("sakura.png"), (800, 600))
background1 = transform.scale(image.load("background2.jpg"), (800, 600))



while game:
    
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if magician_stamina >=1:
                    magician_stamina = magician_stamina - 1
                    magician.fire()
    if magician_stamina <=1:
        Stamina_Cooldown = Stamina_Cooldown + 1
        if Stamina_Cooldown >= 150:
            magician_stamina = magician_stamina + 1
            Stamina_Cooldown = Stamina_Cooldown - 150
    if magician_stamina >3:
        magician_stamina -= 1
    if magician_stamina ==2:
        Stamina_Cooldown = Stamina_Cooldown + 1
        if Stamina_Cooldown >= 150:
            magician_stamina = magician_stamina + 1
            Stamina_Cooldown = Stamina_Cooldown - 150

        


    if level2_active == False and level3_active == False:
        window.blit(background, (0, 0))
    if level2_active == True:
        window.blit(background1, (0, 0))
    if level3_active == True:
        window.blit(background2, (0, 0))
    


    s = font.render("Список:",1,(255,255,255))
    Text = font.render("      : " + str(colletction),1,(255,255,255))
    TextL = font.render("      : " + str(colletction1),1,(255,255,255))
    window.blit(s, (5,60))
    window.blit(Text, (5,100))
    window.blit(TextL, (5,130))
    magician.update()
    magician.reset()
    Icon.update()
    Icon.reset()
    # Отображение HP-бара
    for i in range(magician_health):
        draw.rect(window, (255, 0, 0), (60 + i * 35, 15, 40, 15))
    for i in range(magician_stamina):
        draw.rect(window, (0, 191, 255), (60 + i * 35, 33, 40, 15))
    enemy.reset()
    enemy.update()
    enemy1.reset()
    enemy1.update1()
    bullets.draw(window)
    bullets.update()
    bullets1.update()
    bullets1.draw(window)
    bullets2.update()
    bullets2.draw(window)
    bullets3.update()
    bullets3.draw(window)
    enemy2.update2()
    enemy3.update3()
    enemy5.update4()
    enemy6.update4()
    enemy7.update4()
    icon_clever.reset()
    icon_clever.update()
    icon_glass.reset()
    icon_glass.update()


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
    for cristal in cristals:
        cristal.reset()
    current_time = time.get_ticks()
    if current_time - last_hit_time > HIT_COOLDOWN:
        if sprite.collide_rect(magician, enemy) or sprite.collide_rect(magician, enemy1):
            magician_health -= 1
            last_hit_time = current_time




    if enemy_health ==0:
        enemy.rect.y = -150
    if enemy1_health ==0:
        enemy1.rect.y = -150
    if enemy2_health ==0:
        enemy2.rect.y = -150
    if enemy3_health ==0:
        enemy3.rect.y = -150
    if enemy4_health ==0:
        enemy4.rect.y = -150
    
    
    
    for bullet in bullets:
        if sprite.collide_rect(enemy, bullet):
            enemy_health = enemy_health - 1
            bullet.kill()
            kill_sound.play()
        if sprite.collide_rect(enemy1, bullet):
            enemy1_health = enemy1_health - 1
            bullet.kill()
            kill_sound.play()
        if sprite.spritecollide(enemy2, bullets, True):
            enemy2_health = enemy2_health - 1
            bullet.kill()
            kill_sound.play()
        if sprite.spritecollide(enemy3, bullets, True):
            enemy3_health = enemy3_health - 1
            bullet.kill()
            kill_sound.play()
        if sprite.spritecollide(enemy4, bullets, True):
            enemy4_health = enemy4_health - 1
            bullet.kill()
            kill_sound.play()
        if sprite.spritecollide(boss, bullets, True):
            boss_health = boss_health - 1
            bullet.kill()
            kill_sound.play()
        if sprite.spritecollide(enemy5, bullets, True):
            enemy5_health = enemy5_health - 1
            bullet.kill()
            kill_sound.play()
        if sprite.spritecollide(enemy6, bullets, True):
            enemy6_health = enemy6_health - 1
            bullet.kill()
            kill_sound.play()
        if sprite.spritecollide(enemy7, bullets, True):
            enemy7_health = enemy7_health - 1
            bullet.kill()
            kill_sound.play()

         


    for clever in clevers:
        if sprite.collide_rect(magician, clever):
            colletction = colletction + 1
            clever.kill()
    for cristal in cristals:
        if sprite.collide_rect(magician, cristal):
            colletction = colletction + 1
            cristal.kill()
    for glass in glasses:
        if sprite.collide_rect(magician, glass):
            colletction1 = colletction1 + 1
            glass.kill()
    if sprite.collide_rect(magician, coldron):
        if colletction == 8:
            if colletction1 == 1:
                level_potion.update()
                level_potion.reset()
                colletction = 0
                colletction1 = 0
                if sprite.collide_rect(magician, level_potion):
                    level_potion.kill()
                    colletction2 = 1
    keys = key.get_pressed()
    if keys[K_e] and colletction2 == 1:
        colletction2 = 0
        icon_clever = GameSprite("cristal1.png", 0, 80, 0, 0)
        level_2()
    if level2_active == True:
        current_time = time.get_ticks()
        if current_time - last_hit_time > HIT_COOLDOWN:
            if sprite.collide_rect(magician, enemy2) or sprite.collide_rect(magician, enemy3):
                magician_health -= 1
                last_hit_time = current_time
            if sprite.spritecollide(magician, bullets1, True):
                magician_health -= 1
                last_hit_time = current_time
        if sprite.collide_rect(magician, coldron):
            if colletction == 5:
                if colletction1 == 1:
                    colletction = 0
                    colletction1 = 0
                    level_potion1_collected = True

        if keys[K_e]:
            if level_potion1_collected == True:
                level_potion1_collected = False
                level_3()

            


        if enemy2_health ==0:
            enemy2.rect.y = -150
        if enemy3_health ==0:
            enemy3.rect.y = -150
        if enemy4.rect.y == -150:
            enemy4_stamina = enemy4_stamina - 120
            
        enemy3.reset()
        enemy2.reset()
        enemy4.reset()
        if enemy4_stamina >=1:
                enemy4_stamina = enemy4_stamina - 1
                enemy4.fire()
        if enemy4_stamina <=1:
            Enemy_StaminaCooldown = Enemy_StaminaCooldown + 1
            if Enemy_StaminaCooldown >= 120:
                    enemy4_stamina = enemy4_stamina + 1
                    Enemy_StaminaCooldown = Enemy_StaminaCooldown - 120
    if magician_health == 0:
        magician.rect.x = 50
        magician.rect.y = 500
        game = False
        kill = True
        mixer.music.load('MenuSound.ogg')
        mixer.music.play()
        while kill:
            for e in event.get():
                if e.type==QUIT:
                    kill=False
            background=transform.scale(image.load("Lose.png"),(800,600))
            window.blit(background,(0,0))
            btn_menu.draw(15,5)
            btn_restart.draw(15,5)
            display.update()
            #time.delay(50)
            pos_x, pos_y = mouse.get_pos()
            for e in event.get():
                if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                    menu = True
                    game = False
                    kill = False
                if btn_restart.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                    background = transform.scale(image.load("background.jpg"), (800, 600))
                    window.blit(background,(0,0))
                    mixer.music.load('PlaySound.ogg')
                    mixer.music.play()
                    menu = False
                    game = True
                    kill = False
                    win = False
        while menu:
            for e in event.get():
                if e.type==QUIT:
                    menu=False
            background=transform.scale(image.load("menu.png"),(800,600))
            window.blit(background,(0,0))
            btn_start.draw(15,5)
            btn_end.draw(15,5)
            display.update()
            #time.delay(50)
            pos_x, pos_y = mouse.get_pos()
            for e in event.get():
                if btn_start.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                    background = transform.scale(image.load("background.jpg"), (800, 600))
                    window.blit(background,(0,0))
                    mixer.music.load('PlaySound.ogg')
                    mixer.music.play()
                    menu = False
                    game = True
                    kill = False
                    win = False
                if btn_end.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                    menu = False
                    game = False
                    kill = False
                    win = False
    if magician.rect.x == 50 and magician.rect.y == 500:
        magician_health = 3
    if level2_active == False:
        enemy2.rect.y = -150
        enemy3.rect.y = -150
        enemy4.rect.y = -200
    if level2_enemies == 1 and level2_active:
        enemy2.rect.y = 245
        enemy2.rect.x = 150
        enemy3.rect.y = 295
        enemy3.rect.x = 560
        enemy4.rect.y = 495
        enemy4.rect.x = 740
        level2_enemies = level2_enemies - 1
    if level3_active == False:
        boss.rect.y = -1000
        enemy5.rect.y = -500
        enemy6.rect.y = -500
        enemy7.rect.y = -500
    if level3_active == True:
        boss.rect.y = 310
        boss.rect.x = 564




            
            

    if magician.rect.x < 0:
        magician.rect.x = 50
        magician.rect.y = 500
    if magician.rect.x > 780:
        magician.rect.x = 50
        magician.rect.y = 500
    if magician.rect.y < -50:
        magician.rect.x = 50
        magician.rect.y = 500
    if magician.rect.y > 600:
        magician.rect.x = 50
        magician.rect.y = 500

    if level3_active == True:
        icon_clever.rect.y = - 1000
        icon_glass.rect.y = -1000
        enemy5.reset()
        enemy6.reset()
        enemy7.reset()
        FPS = 90
        clock.tick(FPS)
        boss.reset()
        for i in range(boss_health):
            draw.rect(window, (255, 0, 0), (430 + i * 5, 15, 40, 15))
        for i in range(boss_stamina):
            draw.rect(window, (0, 191, 255), (430 + i * 5, 33, 285, 15))
        if boss_health ==0:
            boss.rect.y = -700
            game = False
            win = True
            mixer.music.load('MenuSound.ogg')
            mixer.music.play()
        while win:
            for e in event.get():
                if e.type==QUIT:
                    win=False
            background=transform.scale(image.load("WinScreen.jpeg"),(800,600))
            window.blit(background,(0,0))
            btn_end1.draw(15,5)
            display.update()
            #time.delay(50)
            pos_x, pos_y = mouse.get_pos()
            for e in event.get():
                if btn_end1.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                    background = transform.scale(image.load("background.jpg"), (800, 600))
                    window.blit(background,(0,0))
                    mixer.music.load('PlaySound.ogg')
                    mixer.music.play()
                    menu = False
                    game = False
                    kill = False
                    win = False
        while menu:
            for e in event.get():
                if e.type==QUIT:
                    menu=False
            background=transform.scale(image.load("menu.png"),(800,600))
            window.blit(background,(0,0))
            btn_start.draw(15,5)
            btn_end.draw(15,5)
            display.update()
            #time.delay(50)
            pos_x, pos_y = mouse.get_pos()
            for e in event.get():
                if btn_start.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                    background = transform.scale(image.load("background.jpg"), (800, 600))
                    window.blit(background,(0,0))
                    mixer.music.load('PlaySound.ogg')
                    mixer.music.play()
                    menu = False
                    game = True
                    kill = False
                    win = False
                if btn_end.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                    menu = False
                    game = False
                    kill = False
                    win = False
        if enemy5_health ==0:
            enemy5.rect.y = -700
        if enemy6_health ==0:
            enemy6.rect.y = -700
        if enemy7_health ==0:
            enemy7.rect.y = -700
        boss_spells = randint(1,3)
        if boss_spells == 1 and boss_stamina == 1:
            boss_spells = randint(1, 3)
            enemy5_health = 2
            enemy6_health =2
            enemy7_health = 2
            enemy7.rect.x = 600
            enemy6.rect.x = 550
            enemy5.rect.x = 510
            boss_stamina = boss_stamina - 1
        if enemy5_health == 2:
            enemy5.rect.y = 486

        if enemy6_health == 2:
            enemy6.rect.y = 486

        if enemy7_health == 2:
            enemy7.rect.y = 486

        if boss_stamina <1:
            BossStamina_Cooldown = BossStamina_Cooldown + 1
        if BossStamina_Cooldown >= 800:
            BossStamina_Cooldown = 0
            boss_stamina = 1
        if boss_spells == 2 and boss_stamina == 1:
            boss.fire()
            boss_spells = randint(1, 3)
            boss_stamina = boss_stamina - 1
            if magician_health <3:
                magician_health = magician_health + 1

        if current_time - last_hit_time > HIT_COOLDOWN:
            if sprite.collide_rect(magician, enemy5) or sprite.collide_rect(magician, enemy6) or sprite.collide_rect(magician, enemy7) or sprite.collide_rect(magician, boss):
                magician_health -= 1
                last_hit_time = current_time
        if sprite.spritecollide(magician, bullets2, True):
                magician_health -= 1
                last_hit_time = current_time

        if boss_spells == 3 and boss_stamina == 1:
            boss.fire1()
            boss_spells = randint(1, 3)
            boss_stamina = boss_stamina - 1

        
        if sprite.spritecollide(magician, bullets3, True):
            magician_health -= 1
            last_hit_time = current_time

    display.update()
    #time.delay(50)
    clock.tick(FPS)
