import pygame
import os
import random

class Bubble:

    max_radius = 80
    min_radius = 20
    max_ticks = 20
    
    def __init__(self, pos):

        x, y = pos
        self.x = x
        self.y = y
        self.radius = 50        
        self.growth = 1
        self.deltax = +1
        self.deltay = -1

        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        a = 128
        color = (r, g, b, a)
        self.color = pygame.Color(color)
        self.ticks = self.max_ticks # Countdown in frames
        
        return

    def grow(self):

        if self.ticks <= 0:
            self.radius = self.radius + self.growth

            if self.radius >= self.max_radius:
                self.growth = 0 - self.growth

            if self.radius <= self.min_radius:
                self.growth = 0 - self.growth
            self.ticks = self.max_ticks
        return
    
    def update(self):

        global screen_width
        global screen_height
        
        self.x = self.x + self.deltax
        self.y = self.y + self.deltay

        if self.x <= 0:
            self.deltax = 0 - self.deltax

        if self.x >= screen_width - ((self.radius * 2)):
            self.deltax = 0 - self.deltax

        if self.y <= 0:
            self.deltay = 0 - self.deltay
        
        if self.y >= screen_height - ((self.radius * 2)):
            self.deltay = 0 - self.deltay
        
        return

    def draw(self):
        surface = pygame.Surface((self.radius*2,self.radius*2))
        surface = surface.convert_alpha()         
       # circle is drawn around circle origin x, y
        pygame.draw.circle(surface, self.color, (self.radius, self.radius), self.radius) 
        screen.blit(surface, (self.x, self.y))
        return

# MAIN

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

while mainloop:
    milliseconds = clock.tick(FPS) # do not go faster than this frame rate
    playtime += milliseconds / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bubbles.append(Bubble(pygame.mouse.get_pos()))
            
    # Do drawing
    screen.blit(background, (0,0))
    for bubble in bubbles:
        bubble.grow()
        bubble.update()
        bubble.draw()
        bubble.ticks = bubble.ticks - 1
    pygame.display.flip()

    
print("this 'game' was played for %.2f seconds" % playtime)
pygame.quit()
 
