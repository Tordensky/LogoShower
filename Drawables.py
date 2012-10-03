'''
Created on Oct 2, 2012

@author: Simon
'''

from Vector2D import *
import pygame

class Drawable(object):
    '''
    classdocs
    '''

    def __init__(self, position = (0, 0)):
        '''
        Constructor
        '''
        self.pos = Vector2D(int(position[0]), int(position[1]))
        
    def draw(self, screen):
        pass
    
class Circle(Drawable):
    '''
    Drawable circle object
    '''
    def __init__(self, position = (0,0), radius = 50, color = (200,200,200)):
        self.pos = Vector2D(position[0] - (radius/4), position[1] - (radius/4))
        self.radius = radius
        self.color = color
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos.get(), self.radius)
        
class Rectangle(Drawable):
    '''
    Drwable rectangle
    '''  
    def __init__(self, position = (0,0), size = (100, 100), color = (255,200,155)):
        self.pos = Vector2D(position[0] - (size[0]/2), position[1] - (size[1]/2))
        self.size = Vector2D(size[0], size[1])
        self.color = color
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos.x, self.pos.y, self.size.x, self.size.y), 1)