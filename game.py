import pygame
import random

pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

color_1 = 200, 120, 100
red = 255, 0, 0
white = 255, 255, 255
black = 0, 0, 0
blue = 0,0,255

def main():
    barWidth = 200
    barHeight = 20
    img = pygame.Surface((barWidth,barHeight))
    img.fill(red)
    barRect = img.get_rect()
    barRect.center  = width/2, height/2
    barRect.y = height - 25
    moveX = 0
    moveX1 = 0
    moveY1 = 0

    brickSurface = pygame.Surface((width-50,175))
    brickSurface.fill(white)

    brickWidth = 100
    brickheight = 30

    brickList = []
    brickColors = []
    for row in range(5):
        for col in range(9):
            brickX = col * (brickWidth+5)
            brickY = row * (brickheight+5)
            color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            brickColors.append(color)
            brickList.append(pygame.Rect(brickX,brickY,brickWidth,brickheight))

    ballSurface = pygame.Surface((8,8))
    ballSurface.fill(blue)
    ballRect = ballSurface.get_rect()

    ballRadius = 8
    ballX = width//2
    ballY = barRect.y - ballRadius

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            if barRect.x > width - 200:
                moveX = 0
                moveX1 = 0
            else:
                moveX = 1
                moveX1 = 1
        elif keypressed[pygame.K_LEFT]:
            if barRect.x < 0:
                moveX = 0
                moveX1 = 0
            else:
                moveX = -1
                moveX1 = -1
        elif keypressed[pygame.K_SPACE]:
            moveX1 = 1
            moveY1 = -1
            if ballX > width - 50:
                moveX1 = -1
            elif ballY < 200:
                moveY1 = 1
            elif ballY > height:
                moveY1 = -1
            elif ballX < 0:
                moveX1 = 1
        else:
            moveX = 0
            moveX1 = 0
            moveY1 = 0

        screen.fill(white)
        screen.blit(img,(barRect.x,barRect.y))
        screen.blit(brickSurface,(30,20))

        for i in range(len(brickList)):
            pygame.draw.rect(brickSurface,brickColors[i],brickList[i])

        pygame.draw.circle(screen,blue,(ballX,ballY),ballRadius)
        #screen.blit(ballSurface, (ballRect.x, ballRect.y))

        barRect.x += moveX
        ballX += moveX1
        ballY += moveY1

        pygame.display.flip()

main()