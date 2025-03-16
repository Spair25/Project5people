from pygame import*

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
font.init()
window=display.set_mode((800,600))
display.set_caption("Магічний котел")
background=transform.scale(image.load("menu.png"),(800,600))
btn_start = Button((66, 49, 133, 1), 260, 350, 280, 70, 'START GAME', 50, (255, 255, 255))
btn_end = Button((66, 49, 133, 1), 260, 445, 280, 70, 'End', 50, (255,255,255))
menu = True
game = False
while menu:
    for e in event.get():
        if e.type==QUIT:
            menu=False
    window.blit(background,(0,0))
    btn_start.draw(15,5)
    btn_end.draw(15,5)
    display.update()
    time.delay(50)
    pos_x, pos_y = mouse.get_pos()
    for e in event.get():
        if btn_start.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
            menu = False
            game = True
        if btn_end.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
            menu = False
            game = False