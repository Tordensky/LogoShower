'''
Created on Sep 16, 2012

@author: Simon
'''
from Drawable import *

import pygame
import time
import random

from pygame.locals import *

class Sprayer():
    def __init__(self, x, y, intesity):
        self.objects = []
        self.x = x
        self.y = y
        
        self.intesity = intesity
        self.counter = 0
        
        # Color
        self.red_min = 0
        self.red_max = 255
        self.green_min = 0
        self.green_max = 255
        self.blue_min = 0
        self.blue_max = 225
        
        
        
    def update_and_paint(self, screen, time_passed_seconds):
        # Draw objects to screen
        
        color = (random.randrange(self.red_min, self.red_max), random.randrange(self.green_min, self.green_max),  random.randrange(self.blue_min, self.blue_max), 20)
        
        self.counter += 1
        
        if (self.counter == self.intesity):
            self.counter = 0  
            self.objects.append(MovableCircle(self.x, self.y, random.randrange(-100, 100), random.randrange(-300, 100), radius=random.randrange(5, 10), color=color, grav=0.5))
        
        
        for obj in self.objects:
            if (obj.out_of_bounds(screen)):
                self.objects.remove(obj)
            else:
                obj.move(time_passed_seconds)
                obj.draw(screen)
        

class LogoShower():
    def __init__(self):
        """ Main program """
        
        # Set up pygame
        print pygame.init()
        self.screen = pygame.display.set_mode((1280, 768), pygame.FULLSCREEN )
        pygame.display.set_caption('Labyrinth')
        
        self.bckimage = pygame.image.load('grafikk/background.png').convert()
        self.logo = pygame.image.load('grafikk/logo.png').convert_alpha()
        
        self.drawable = []


    def main(self):
        
        pos_x = (self.screen.get_width() / 2) - (self.logo.get_width() / 2)
        pos_y = (self.screen.get_height() / 2) - (self.logo.get_height() / 2)
        
        num_sprayers = 6
        
        clock = pygame.time.Clock()
        sprayers = []
        for x in range(1, num_sprayers+1):
            pos = x * (self.screen.get_width() / (num_sprayers+1))
            sprayers.append(Sprayer(pos, pos_y + (self.logo.get_height() / 2), 2))
        
        #sprayers = [Sprayer(100, 200, 1), Sprayer(300, 200, 1), Sprayer(500, 200, 1), Sprayer(700, 200, 1), Sprayer(900, 200, 1)]
        #sprayers += [Sprayer(200, 200, 1), Sprayer(400, 200, 1), Sprayer(600, 200, 1), Sprayer(800, 200, 1)]
        
        
        
        
        
        while (True):
            for event in pygame.event.get():
                    if event.type == QUIT:
                        return
                    elif event.type == KEYDOWN:          
                        if event.key == K_ESCAPE:
                            return
            
            time_passed = clock.tick(100) # limit to x FPS 
            time_passed_seconds = time_passed / 1000.0
            
            self.screen.fill((0,0,0))
            
            #self.screen.blit(self.bckimage, (0,0))
            
            for sprayer in sprayers:
                sprayer.update_and_paint(self.screen, time_passed_seconds)
            
            
            
            self.screen.blit(self.logo, (pos_x,pos_y))
                
            pygame.display.flip()
        


if __name__ == '__main__':
    logoShower = LogoShower()
    logoShower.main()