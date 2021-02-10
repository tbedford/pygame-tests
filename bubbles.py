import pygame
import os
import random

class Bubble:

    deltax = +2
    deltay = -2
    growth = 1
    max_radius = 100
    min_radius = 10
    radius = 20
    speed = 2
    
    # create bubble at origin x, y
    def __init__(self, pos):

        x, y = pos
        self.x = x - self.max_radius
        self.y = y - self.max_radius

        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        a = 128
        color = (r, g, b, a)
        self.color = pygame.Color(color)
#        
        return

    def grow(self):

        if self.radius >= self.max_radius:
            self.growth = -1
            print("Exceeded max radius: ", self.growth)

        if self.radius <= self.min_radius:
            self.growth = +1
            print("Exceeded min radius: ", self.growth)
            
        self.radius = self.radius + self.growth
        pygame.display.set_caption("Radius: %d" % self.radius)
        return
    
    def update(self):

        global screen_width
        global screen_height
        
        if self.x <= 0:
            self.deltax = 0 - self.deltax

        if self.x >= screen_width - (self.radius * 2):
            self.deltax = 0 - self.deltax

        if self.y <= 0:
            self.deltay = 0 - self.deltay
        
        if self.y >= screen_height - (self.radius * 2):
            self.deltay = 0 - self.deltay

        self.x = self.x + self.deltax
        self.y = self.y + self.deltay
        
        return

    def draw(self):
         # Each bubble has its own surface
        self.surface = pygame.Surface((self.max_radius*2,self.max_radius*2))
        self.surface = self.surface.convert_alpha()         
       # circle is drawn around circle origin x, y
        pygame.draw.circle(self.surface, self.color, (self.max_radius, self.max_radius), self.radius) 
        screen.blit(self.surface, (self.x, self.y))
        return
    
screen_width = 640
screen_height = 480

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.Surface(screen.get_size()).convert()
emily_art = pygame.image.load(os.path.join("data", 'emily_art.png')).convert()
pygame.transform.scale(emily_art, (screen_width, screen_height), background)
screen.blit(background, (0,0))

clock = pygame.time.Clock()
mainloop = True
FPS = 60 
playtime = 0.0
bubbles = []
ticks = 0

while mainloop:
    ticks = ticks + 1
    milliseconds = clock.tick(FPS) # do not go faster than this frame rate
    playtime += milliseconds / 1000.0
    # ----- event handler -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print('Mouse down event type')
            bubble = Bubble(pygame.mouse.get_pos())
            bubbles.append(bubble)
            
    # Do drawing
    screen.blit(background, (0,0))
    for bubble in bubbles:
        #bubble.update()
        bubble.draw()
        if ticks > 2:
            bubble.grow()
            ticks = 0
    pygame.display.flip()

    
print("this 'game' was played for %.2f seconds" % playtime)
pygame.quit()
 
