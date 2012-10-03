'''
Created on Oct 2, 2012

@author: Simon
'''

import pygame
from Drawables import *
from pygame.locals import *

class Game(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pygame.init()
        
        self.screen = pygame.display.set_mode((800, 600))
        
        self.drawables = [Rectangle((200, 200)), Circle((200, 200))]
        
    def run(self):
        
        clock = pygame.time.Clock()
        
        while (True):
            for event in pygame.event.get():
                    if event.type == QUIT:
                        return
                    elif event.type == KEYDOWN:          
                        if event.key == K_ESCAPE:
                            return
            
            time_passed = clock.tick(30) # limit to x FPS 
            time_passed_seconds = time_passed / 1000.0
            
            self.screen.fill((0,0,0))
            
            self.move_objects(time_passed_seconds)
            
            self.draw_objects()
                        
            pygame.display.flip()
    
    def move_objects(self, time_passed_seconds):
        pass
            
    def draw_objects(self):
        for obj in self.drawables:
            obj.draw(self.screen)
        
            
            
if __name__ == "__main__":
    game = Game()
    game.run()