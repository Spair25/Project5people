from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
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
        if keys[K_RIGHT] and self.rect.x <650:
            self.rect.x += self.speed

window=display.set_mode((800,600))
display.set_caption("Магічний котел")
background=transform.scale(image.load("background.jpg"),(800,600))

game=True
clock=time.Clock()
FPS=60

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    window.blit(background,(0,0))

    display.update()
    time.delay(50)
    clock.tick(FPS)
