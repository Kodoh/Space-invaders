import pygame


#initialize pygame
pygame.init()
#create the screen

screen = pygame.display.set_mode((800,600))
background = pygame.image.load("menu.JPG")
pygame.display.set_caption("Jakes Space Invaders - Menu")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)


running = True
while running:

    #RGB - red,green,blue
    screen.fill((255,255,255))
    screen.blit(background, (0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                import main
                running = False
            if event.key == pygame.K_4:
                import credit
                running = False 

    

    
    

pygame.display.update()

