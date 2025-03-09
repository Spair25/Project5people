class Player():
    def Update(self):
        Keys = key.get_pressed()
        if Keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if Keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        if Keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if Keys[K_s] and self.rect.x < 450:
            self.rect.y += self.speed

while Manegment:
    for e in event.get():
        if e.type == QUIT:
            Game = False
        elif: e.type == KEYDOWN:
            if e.key == K_SPACE:
                Player.fire()

        if(sprite.collide_rect(Player, Wall)):
            Player.rect.x = 50
            Player.rect.y = 400
