import pygame
import os

pygame.init()

width = 640
height = 480

r = 255
g = 50
b = 50
a = 255

w = 200
h = 100

pygame.mouse.set_visible(True)

screen = pygame.display.set_mode((width,height))

background = pygame.Surface(screen.get_size())
background.fill((0,128,100))
background = background.convert()
screen.blit(background, (0, 0))

startx = 20
starty = 20

player_surface = pygame.Surface((w+300,w+100))
pygame.draw.rect(player_surface, (r, g, b, a), (startx, starty, w, h)) # rect: (x1, y1, width, height)
player_surface = player_surface.convert()
screen.blit(player_surface, (0, 0))

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Mouse down event type')
        elif event.type == pygame.MOUSEBUTTONUP:
            print('Mouse up event type')
        elif event.type == pygame.MOUSEMOTION:
            print('Mouse motion event type')
                
    pos_x, pos_y = pygame.mouse.get_pos()
    text = "Mouse x: %d Mouse y: %d" % (pos_x, pos_y)
    pygame.display.set_caption(text)
    pygame.display.flip()

print(pygame.mouse.get_visible())
pygame.quit()
 
