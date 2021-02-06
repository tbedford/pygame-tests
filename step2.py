import pygame
pygame.init()

screen = pygame.display.set_mode((640,480)) # Set screen size of pygame window
background = pygame.Surface(screen.get_size())  # Create empty pygame surface
background.fill((0,128,100))     # Fill the background white color (red,green,blue)
background = background.convert()  # Convert Surface to make blitting faster

screen.blit(background, (0, 0))
clock = pygame.time.Clock()

mainloop = True
# Desired framerate in frames per second. Try out other values.              
FPS = 30
# How many seconds the "game" is played.
playtime = 0.0
 
while mainloop:
    # Do not go faster than this framerate.
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0 
     
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                mainloop = False
                 
    # Print framerate and playtime in titlebar.
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    pygame.display.set_caption(text)
 
    #Update Pygame display.
    pygame.display.flip()
 
# Finish Pygame.  
pygame.quit()
 
# At the very last:
print("This game was played for {0:.2f} seconds".format(playtime))
