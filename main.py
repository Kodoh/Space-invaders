import pygame
import random
import math

from pygame import mixer

#initialize pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600))     #800 wide 600 height


#background
background = pygame.image.load("background2.png")


#background music
mixer.music.load("background.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.05)

#title + icon
pygame.display.set_caption("Jakes Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)
#game loop 

#Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480           #coords for spaceship 
playerx_change = 0 

#Enemy 
enemyImg = []
enemyX = []
enemyY = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):

    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))          #coords for spaceship 
    enemyx_change.append(4)
    enemyy_change.append(40)

#bullet
#Ready state = you cant see the bullet on the screen
#Fire = the bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480        #coords for spaceship 
bulletx_change = 0
bullety_change = 10
bullet_state = "ready" 

#score
score_value =  0
font = pygame.font.Font("freesansbold.ttf",32) #free pygame font without having to download fonts



# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)





textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score : " + str(score_value),True, (252,133,153))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    over_menu = font.render("Press esc to go back to menu", True, (225, 255, 255))
    screen.blit(over_menu, (200,150))

                



def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, ( x + 16, y + 10))


def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27: #the distance between them is less than 27 pixels 
        return True 
    else:
        return False

def player(x,y):
    screen.blit(playerImg, (x,y)) #drawing image on screen

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y)) #drawing image on screen

running = True
while running:

    #RGB - red,green,blue
    screen.fill((34,181,156))
    #background image
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# checks if left or right key 


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletSound.set_volume(0.05)
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
            
                

    playerX += playerx_change
    

    #enemy boundaries
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        import menu
                        running = False
            break


        enemyX[i] += enemyx_change[i]
        if enemyX[i] <= 0:
            enemyx_change[i] = 4
            enemyY[i] += enemyy_change[i]
        elif enemyX[i] >= 736: # 800 - 64(becuase 64x64 bit spaceship image)
            enemyx_change[i] = -4
            enemyY[i] += enemyy_change[i]

        
        # collision 
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        #if true
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            explosionSound.set_volume(0.05)
            bulletY = 480 
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
        

    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bullety_change



    #player boundaries
    if playerX <= 0:
        playerX = 0 
    elif playerX >= 736: # 800 - 64(becuase 64x64 bit spaceship image)
        playerX = 736
    player(playerX,playerY)
    
    show_score(textX,textY)

    enemyX += enemyx_change

    pygame.display.update()
    

    


