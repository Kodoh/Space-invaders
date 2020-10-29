import pygame


#initialize pygame
pygame.init()
#create the screen

screen = pygame.display.set_mode((800,600))
background = pygame.image.load("menu.JPG")
pygame.display.set_caption("Jakes Space Invaders - Credits")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)


over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render("Credits: Jake", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

memeImg = pygame.image.load("meme.png")

#memeX = 370
#memeY = 480
def meme(x,y):
    screen.blit(memeImg, (x,y))



running = True
while running:
    #RGB - red,green,blue
    screen.fill((225,225,240))
    game_over_text()
    meme(300,350)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


pygame.display.update()