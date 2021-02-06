import pygame
import os

pygame.init()

width = 1280
height = 960
ballx = 640
bally = 480
r = 255
g = 50
b = 50
a = 128
w = 200

screen = pygame.display.set_mode((width,height))

background = pygame.Surface(screen.get_size()).convert()
emily_art = pygame.image.load(os.path.join("data", 'emily_art.png')).convert()
pygame.transform.scale(emily_art, (width, height), background)
screen.blit(background, (0,0))

ballsurface = pygame.Surface((w,w))
pygame.draw.circle(ballsurface, (r,g,b,a), (w/2,w/2), w/2)
ballsurface = ballsurface.convert_alpha()
screen.blit(ballsurface, (ballx, bally))

clock = pygame.time.Clock()
mainloop = True
FPS = 30
 
while mainloop:
    # Do not go faster than this framerate.
    milliseconds = clock.tick(FPS) 
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            elif event.key == pygame.K_UP:
                if a < 255:
                    a = a + 1
            elif event.key == pygame.K_DOWN:
                if a > 0:
                    a = a - 1
            elif event.key == pygame.K_SPACE:
                mainloop = False

    screen.blit(background, (0,0))            
    pygame.draw.circle(ballsurface, (r,g,b, a), (w/2,w/2), w/2)
    screen.blit(ballsurface, (ballx, bally))                 
    pygame.display.flip()
 
pygame.quit()
 
