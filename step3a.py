import pygame

def move_ball(x, y):

    global deltax
    global deltay
    
    if x <= 0:
        deltax = 0 - deltax

    if x >= 640 - 50:
        deltax = 0 - deltax

    if y <= 0:
        deltay = 0 - deltay
        

    if y >= 480 - 50:
        deltay = 0 - deltay

    x = x + deltax
    y = y + deltay
        
    return x, y
        
pygame.init()
screen = pygame.display.set_mode((640,480))

background = pygame.Surface(screen.get_size())
background.fill((0,0,0))
background = background.convert()

ball_color = pygame.Color(255,0,0,10)
ballsurface = pygame.Surface((50,50))
pygame.draw.circle(ballsurface, ball_color, (25,25),25) 
ballsurface = ballsurface.convert() 

ballx = 320
bally = 240
 
screen.blit(background, (0,0))
screen.blit(ballsurface, (ballx, bally))

clock = pygame.time.Clock()
mainloop = True
FPS = 60 # desired framerate in frames per second. try out other values !
playtime = 0.0

deltax = -4
deltay = 4
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
    pygame.display.flip()      # flip the screen like in a flipbook
print("this 'game' was played for %.2f seconds" % playtime)
