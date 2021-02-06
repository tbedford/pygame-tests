import pygame

pygame.init()

screen = pygame.display.set_mode((640,480)) # Set screen size of pygame window

background = pygame.Surface(screen.get_size())  # Create empty pygame surface
background.fill((0,128,100))     # Fill the background white color (red,green,blue)
background = background.convert()  # Convert Surface to make blitting faster
screen.blit(background, (0, 0))

w = 100
ballsurface = pygame.Surface((w,w)).convert()
pygame.draw.circle(ballsurface, (0,0,128), (w/2,w/2), w/2) 
ballx = 320
bally = 240
screen.blit(ballsurface, (ballx, bally))

clock = pygame.time.Clock()
mainloop = True
FPS = 30
 
while mainloop:
    # Do not go faster than this framerate.
    milliseconds = clock.tick(FPS) 
      
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                mainloop = False
                 
    pygame.display.flip()
 
pygame.quit()
 
