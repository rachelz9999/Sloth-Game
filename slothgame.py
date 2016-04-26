
#import pygame
import pygame, sys
import random, sys
from pygame.locals import *
pygame.init()

def playerEnemyCollided(playerx, playery, enemyx, enemyy):
    slothx = playerx + 0.5*(120)
    slothy = playery + 0.5*(120)
    nyquilx = enemyx + 0.5*(70)
    nyquily = enemyy + 0.5*(90)
    distance = ((slothx - nyquilx)**2 + (slothy - nyquily)**2)**(0.5)
    if distance <= 100:
        return True
    else:
        return False
    
def playerEnemyCollided(playerx, playery, enemyx, enemyy):
    slothx = playerx + 0.5*(120)
    slothy = playery + 0.5*(120)
    Frapx = enemyx + 0.5*(70)
    Frapy = enemyy + 0.5*(90)
    distance = ((slothx - Frapx)**2 + (slothy - Frapy)**2)**(0.5)
    if distance <= 100:
        return True
    else:
        return False
        
#creating the window
window = pygame.display.set_mode((800,600)) #tuple
pygame.display.set_caption("Grand Theft Slotho")

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,153,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)
orange = (255,155,0)
royal = (107,181,255)
sea = (107,255,188)

#text
myFont = pygame.font.SysFont("arial",72)
myText = myFont.render("Grand Theft Slotho", True, royal)
window.blit(myText, (200,200))


#image
treeImage = pygame.image.load("tree3.jpg")
window.blit(treeImage, (0,0))
                              
slothImage = pygame.image.load("sloth.jpg")
window.blit(slothImage, (0, 100) )

nyquilImage = pygame.image.load("nyquil.jpg")
nyquilresized = pygame.transform.scale (nyquilImage, (70, 90))

FrapImage = pygame.image.load("Frap.jpg")
FrapResized = pygame.transform.scale (FrapImage, (60,80))

loseImage = pygame.image.load("losesloth.jpg")
loseresized = pygame.transform.scale (loseImage, (800,600))

HeartImage = pygame.image.load("Heart.png")
Heartresized = pygame.transform.scale(HeartImage, (20,20))

xImage = pygame.image.load("x.png")
xresized = pygame.transform.scale(xImage, (20,20))

winImage = pygame.image.load("WinnerCarSloth.jpg")
winresized = pygame.transform.scale (winImage, (800,600))

startImage = pygame.image.load("start.jpg")
startresized = pygame.transform.scale(startImage, (800,600))

start2Image = pygame.image.load("level2.jpg")
start2resized = pygame.transform.scale(start2Image, (800,600))

#animation
tree = pygame.image.load("tree3.jpg")
treeresized = pygame.transform.scale (treeImage, (700,1700))
treex = 50
treey = -600
window.blit(tree, (treex, treey) )

sloth = pygame.image.load("sloth.jpg")
slothx = 100
slothy = 450
window.blit(sloth, (slothx, slothy) )


winLevel1 = False
winLevel2 = False
winLevel3 = False

#enemies
nyquilList = [ [100,0], [650,0] ]
FrapList = [ [200,0], [500,0] ]

for i in range(3):
    nyquilx = random.randrange(0, 400)
    nyquilList.append([nyquilx, 0])

for i in range(1):
    Frapx = random.randrange(0, 400)
    FrapList.append([Frapx, 0])
    
start = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                start = True
    startscreen = startresized
    window.blit(startscreen, (0,0))
    pygame.display.update()
    if start == True:
        break

#Level 1
lives = 3
score = 0
WinOrLose = "just started"
count = 0
done = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                slothx += 30
            elif event.key == K_LEFT:
                slothx -= 30
        treey += 3
        if treey >= 0:
            treey = -600

    
    
    window.fill(royal)
        
    window.blit(treeresized, (treex, treey))
    window.blit(sloth, (slothx, slothy))
                
    #text
    myFont = pygame.font.SysFont("impact",72)
    myText = myFont.render("Grand Theft Slotho", True, green, royal)
    window.blit(myText, (130,50))

    
    for i in range(len(nyquilList)):
        window.blit(nyquilresized, (nyquilList[i][0], nyquilList[i][1]))
        nyquilList[i][1] += 2
        #if playerEnemyCollided((slothx, slothy), (nyquilList[i][0], nyquilList[i][1])) == True:
            #WinOrLose = "Lose"
        if playerEnemyCollided((slothx, slothy), (nyquilList[i][0], nyquilList[i][1])) == True:
            lives = lives - .01
        if nyquilList[i][1] > 600:
            nyquil_new_x = random.randint(0,800)
            nyquilList[i][0] = nyquil_new_x
            nyquilList[i][1] = 0
   
    for i in range(len(FrapList)):
        window.blit(FrapResized, (FrapList[i][0], FrapList[i][1]))
        FrapList[i][1] += 2
        if FrapList[i][1] > 600:
            Frap_new_x = random.randint(0,800)
            FrapList[i][0] = Frap_new_x
            FrapList[i][1] = 0
        if playerEnemyCollided((slothx, slothy), (FrapList[i][0], FrapList[i][1])) == True:
            score += 1

    window.blit(Heartresized, (350, 20))
    window.blit(Heartresized, (400, 20))
    window.blit(Heartresized, (450, 20))
    if int(lives) <=2:
        window.blit(xresized, (350,20))
    if int(lives) <=1:
        window.blit(xresized, (400,20))
    if int(lives) <=0:
        window.blit(xresized, (450,20))

    myFont= pygame.font.SysFont('Small Fonts', 30)
    myText = myFont.render("Score: " + str(score), True, black, white)
    window.blit(myText, (80,20))
        
    if int(lives) == 0:
        WinOrLose = "Lose"
    if score >= 1000:
        winLevel1 = "Win"
    
    if winLevel1 == "Win":
        break
    if WinOrLose == "Lose":
        break
    
    pygame.display.update()

#to Level 2
start2 = False
while winLevel1 == "Win":
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                print ("pressed space")
                start2 = True
    start2screen = start2resized
    window.blit(start2screen, (0,0))
    pygame.display.update()
    if start2 == True:
        print ("start2")
        break

#Level 2
if winLevel1 == "Win":
    lives = 3
    score = 0
    WinOrLose = "just started"
    count = 0
    done = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    slothx += 30
                elif event.key == K_LEFT:
                    slothx -= 30
            treey += 3
            if treey >= 0:
                treey = -600

        
        
        window.fill(royal)
            
        window.blit(treeresized, (treex, treey))
        window.blit(sloth, (slothx, slothy))
                    
        #text
        myFont = pygame.font.SysFont("impact",72)
        myText = myFont.render("Grand Theft Slotho", True, green, royal)
        window.blit(myText, (130,50))

        
        for i in range(len(nyquilList)):
            window.blit(nyquilresized, (nyquilList[i][0], nyquilList[i][1]))
            nyquilList[i][1] += 4
            #if playerEnemyCollided((slothx, slothy), (nyquilList[i][0], nyquilList[i][1])) == True:
                #WinOrLose = "Lose"
            if playerEnemyCollided((slothx, slothy), (nyquilList[i][0], nyquilList[i][1])) == True:
                lives = lives - .01
            if nyquilList[i][1] > 600:
                nyquil_new_x = random.randint(0,800)
                nyquilList[i][0] = nyquil_new_x
                nyquilList[i][1] = 0
       
        for i in range(len(FrapList)):
            window.blit(FrapResized, (FrapList[i][0], FrapList[i][1]))
            FrapList[i][1] += 3
            if FrapList[i][1] > 600:
                Frap_new_x = random.randint(0,800)
                FrapList[i][0] = Frap_new_x
                FrapList[i][1] = 0
            if playerEnemyCollided((slothx, slothy), (FrapList[i][0], FrapList[i][1])) == True:
                score += 1

        window.blit(Heartresized, (350, 20))
        window.blit(Heartresized, (400, 20))
        window.blit(Heartresized, (450, 20))
        if int(lives) <=2:
            window.blit(xresized, (350,20))
        if int(lives) <=1:
            window.blit(xresized, (400,20))
        if int(lives) <=0:
            window.blit(xresized, (450,20))

        myFont= pygame.font.SysFont('Small Fonts', 30)
        myText = myFont.render("Score: " + str(score), True, black, white)
        window.blit(myText, (80,20))
            
        if int(lives) == 0:
            WinOrLose = "Lose"
        if score >= 1000:
            winLevel2 = "Win"
        
        if winLevel2 == "Win":
            break
        if WinOrLose == "Lose":
            break
        
        pygame.display.update()

#to Level 3
start3 = False
while winLevel2 == "Win":
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                print ("pressed space")
                start3 = True
    start3screen = start2resized
    window.blit(start3screen, (0,0))
    pygame.display.update()
    if start3 == True:
        print ("start3")
        break

#Level 3
if winLevel2 == "Win":
    lives = 3
    score = 0
    WinOrLose = "just started"
    done = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    slothx += 30
                elif event.key == K_LEFT:
                    slothx -= 30
            treey += 3
            if treey >= 0:
                treey = -600

        
        
        window.fill(royal)
            
        window.blit(treeresized, (treex, treey))
        window.blit(sloth, (slothx, slothy))
                    
        #text
        myFont = pygame.font.SysFont("impact",72)
        myText = myFont.render("Grand Theft Slotho", True, green, royal)
        window.blit(myText, (130,50))

        
        for i in range(len(nyquilList)):
            window.blit(nyquilresized, (nyquilList[i][0], nyquilList[i][1]))
            nyquilList[i][1] += 8
            #if playerEnemyCollided((slothx, slothy), (nyquilList[i][0], nyquilList[i][1])) == True:
                #WinOrLose = "Lose"
            if playerEnemyCollided((slothx, slothy), (nyquilList[i][0], nyquilList[i][1])) == True:
                lives = lives - .01
            if nyquilList[i][1] > 600:
                nyquil_new_x = random.randint(0,800)
                nyquilList[i][0] = nyquil_new_x
                nyquilList[i][1] = 0
       
        for i in range(len(FrapList)):
            window.blit(FrapResized, (FrapList[i][0], FrapList[i][1]))
            FrapList[i][1] += 5
            if FrapList[i][1] > 600:
                Frap_new_x = random.randint(0,800)
                FrapList[i][0] = Frap_new_x
                FrapList[i][1] = 0
            if playerEnemyCollided((slothx, slothy), (FrapList[i][0], FrapList[i][1])) == True:
                score += 1

        window.blit(Heartresized, (350, 20))
        window.blit(Heartresized, (400, 20))
        window.blit(Heartresized, (450, 20))
        if int(lives) <=2:
            window.blit(xresized, (350,20))
        if int(lives) <=1:
            window.blit(xresized, (400,20))
        if int(lives) <=0:
            window.blit(xresized, (450,20))

        myFont= pygame.font.SysFont('Small Fonts', 30)
        myText = myFont.render("Score: " + str(score), True, black, white)
        window.blit(myText, (80,20))
            
        if int(lives) == 0:
            WinOrLose = "Lose"
        if score >= 1000:
            WinOrLose = "Win"
        
        if WinOrLose == "Win":
            break
        if WinOrLose == "Lose":
            break
        
        pygame.display.update()

#draw game over
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if WinOrLose == "Lose":
        gameOverScreen = loseresized
        window.blit(gameOverScreen, (0,0))
        pygame.display.update()
    elif WinOrLose == "Win":
        winScreen = winresized
        window.blit(winScreen,(0,0))
        pygame.display.update()
