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
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <650:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self,f,t):
        if self.rect.x<=f:
            self.direction = "right"
        if self.rect.x >= t:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update1(self):
        if self.rect.x<=600:
            self.direction = "right"
        if self.rect.x >=730:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
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
        self.txt_image = font.Font('font/impact.ttf', fsize).render(text, True, txt_color)

    def draw(self, shift_x, shift_y): # цей метод малює кнопку із тектом в середині. Сам текст зміщенний на величини shift_x та shift_y
        win.blit(self.image, (self.rect.x, self.rect.y))
        win.blit(self.txt_image, (self.rect.x + shift_x, self.rect.y + shift_y))            
window=display.set_mode((800,600))
display.set_caption("Магічний котел")
background=transform.scale(image.load("background.jpg"),(800,600))

# завантажуємо звуки
mixer.init()
# звуки під час подій 
#click=mixer.Sound('музичний файл.ogg')


level=["                " ,
       "            0 +u",
       "            ----",
       "                ",
       "    8           ",
       "  + H           ",
       "  - H        +  ",
       "+   H    +  H-- ",
       "--      --  H   ",
       "    ---     H   ",
       "+        +     0",
       "----------------"]

platforms=sprite.Group()
portals=sprite.Group()
coldrons=sprite.Group()
leders=sprite.Group()
glasses=sprite.Group()
clevers=sprite.Group()
magician=Player("magician.png",50,500,50,50,10)
enemy = Enemy("enemy.png", 725, 486, 5, 0)
enemy1 = Enemy("enemy.png", 743, 286, 5, 0)
x=0
y=0
for plt in level:
    x=0
    for p in plt:
        if p=="-":
            platform=GameSprite('platform.png',x,y,50,50,0)
            platforms.add(platform)
        if p=="0":
            portal=GameSprite('portale.png',x,y,50,50,0)
            portals.add(portal)
        if p=="u":
            coldron=GameSprite('coldron.png',x,y,50,50,0)
            coldrons.add(coldron)
        if p=="H":
            leder=GameSprite('leder.png',x,y,50,50,0)
            leders.add(leder)
        if p=="8":
            glass=GameSprite('glass.png',x,y,50,50,0)
            glasses.add(glass)
        if p=="+":
            clever=GameSprite('clever.png',x,y,50,50,0)
            clevers.add(clever)
        x+=50
    y+=50


kaunt= 0

game=True
clock=time.Clock()
FPS=60

font.init()
font = font.Font(None, 70)
font2 = font.SysFont('Arial', 50)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

lose2=transform.scale(image.load("lose.png"),(700,500))
win2 = transform.scale(image.load("semya.jpg"),(700,500))

text = font2.render(""+ str(kaunt),1, (255, 255, 255))
window.blit(text, (10,20))

while game:
    # фонова музика
    #mixer.music.load('game.ogg')
    #mixer.music.play()
    for e in event.get():
        if e.type==QUIT:
            game=False
    magician.rect.y += magician.speed
    if sprite.spritecollide(magician,platforms, False):
         magician.rect.y -= magician.speed
    keys = key.get_pressed()
    if keys[K_UP] and magician.rect.y > 20 and sprite.spritecollide(magician,platforms, False):
        magician.rect.y -= magician.jump
    
    window.blit(background,(0,0))
    magician.reset()
    magician.update()  
    enemy.reset()
    enemy.update()
    enemy1.reset()
    enemy1.update1()
    for platform in platforms:
        platform.reset()
    for portal in portals:
        portal.reset()
    for coldron in coldrons:
        coldron.reset()
    for leder in leders:
        leder.reset()
    for glass in glasses:
        glass.reset()
    for clever in clevers:
        clever.reset()
        
    display.update()
    time.delay(50)
    clock.tick(FPS)
  
    #click.play()
# когда премия? никогда! почему?
# когда премия? никогда! почему?
# когда премия? никогда! почему?
# когда премия? никогда! почему?
# когда премия? никогда! почему?
# когда премия? никогда! почему?
# когда премия? никогда! почему?
