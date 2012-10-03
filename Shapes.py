'''
Created on Sep 16, 2012

@author: Simon
'''
import pygame

class Drawable(object):
    '''
    A class for drawable objects
    '''

    def __init__(self, pos_x = 0, pos_y = 0):
        '''
        Constructor
        '''
        self.pos = (pos_x, pos_y)
            
    def draw(self, screen):
        '''
        Method for drawing object to screen
        '''
        pass
    
   
    
class Circle(Drawable):
    def __init__(self, pos_x = 0, pos_y = 0, color=(255,0,0), radius=10):
        Drawable.__init__(self, pos_x, pos_y)
        self.color = color
        self.radius = radius
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius) 
        
    
class MovableDrawable(Drawable):
    '''
    A class for movable drawable objects
    '''
    
    def __init__(self, pos_x = 0, pos_y = 0, speed_x = 0, speed_y = 0, grav=10):
        Drawable.__init__(self, pos_x, pos_y)
        self.speed = (speed_x, speed_y)
        self.grav = grav
    
    def move(self, time_passed_seconds):
        '''
        Method for move object to new position
        '''
        x, y = self.pos
        sx, sy = self.speed
        
        sy += self.grav
        
        x = (x + sx * time_passed_seconds)
        y = (y + sy * time_passed_seconds) 
        
        self.pos = (x, y)
        self.speed = (sx, sy)
    
    def out_of_bounds(self, screen):
        if (screen.get_height() < self.pos[1]):
            return True
        return False
    
class MovableCircle(MovableDrawable, Circle):
    def __init__(self, pos_x = 0, pos_y = 0, speed_x = 0, speed_y = 0, color=(255,0,0), radius=10, grav=10):
        Circle.__init__(self, pos_x, pos_y, color, radius)
        MovableDrawable.__init__(self, pos_x, pos_y, speed_x, speed_y, grav)
    
        