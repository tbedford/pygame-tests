import pygame
import os

def move_ball(x, y):

    global deltax
    global deltay
    global width
    global height
    
    if x <= 0:
        deltax = 0 - deltax

    if x >= width - (ball_radius * 2):
        deltax = 0 - deltax

    if y <= 0:
        deltay = 0 - deltay
        

    if y >= height - (ball_radius * 2):
        deltay = 0 - deltay

    x = x + deltax
    y = y + deltay
        
    return x, y

width = 1280
height = 960
ball_radius = 100
ballx = 320
bally = 240

pygame.init()
screen = pygame.display.set_mode((width, height))

background = pygame.Surface(screen.get_size()).convert()
emily_art = pygame.image.load(os.path.join("data", 'emily_art.png')).convert()
pygame.transform.scale(emily_art, (width, height), background)
screen.blit(background, (0,0))

ball_color = pygame.Color(10,200,0,128)
ballsurface = pygame.Surface((ball_radius*2,ball_radius*2))
pygame.draw.circle(ballsurface, ball_color, (ball_radius, ball_radius), ball_radius) 
ballsurface = ballsurface.convert_alpha() 
screen.blit(ballsurface, (ballx, bally))

clock = pygame.time.Clock()
mainloop = True
FPS = 60 # desired framerate in frames per second. try out other values !
playtime = 0.0

deltax = -2
deltay = 2
x = ballx
y = bally
while mainloop:
    milliseconds = clock.tick(FPS) # do not go faster than this frame rate
    playtime += milliseconds / 1000.0
    # ----- event handler -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC
    pygame.display.set_caption("Frame rate: {:0.2f} frames per second." 
                               " Playtime: {:.2} seconds".format(
                               clock.get_fps(),playtime))
    x, y = move_ball(x, y)
    screen.blit(background, (0,0))
    screen.blit(ballsurface, (x, y))
    pygame.display.flip()      
print("this 'game' was played for %.2f seconds" % playtime)
