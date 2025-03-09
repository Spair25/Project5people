from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <750:
            self.rect.x += self.speed

window=display.set_mode((800,600))
display.set_caption("Магічний котел")
background=transform.scale(image.load("background.jpg"),(800,600))

magician=Player("magician.png",50,500,10)

game=True
clock=time.Clock()
FPS=60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

lose2=transform.scale(image.load("lose.png"),(700,500))
win2 = transform.scale(image.load("semya.jpg"),(700,500))

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
            
    window.blit(background,(0,0))
    magician.reset()
    magician.update()  

    display.update()
    time.delay(50)
    clock.tick(FPS)
