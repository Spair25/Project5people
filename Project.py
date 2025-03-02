from pygame import * 

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
