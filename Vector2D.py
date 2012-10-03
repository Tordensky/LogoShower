'''
Created on Oct 2, 2012

@author: Simon
'''

import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "Vector(%s, %s)" % (self.x, self.y)
        
    def __add__(self, b):
        return Vector2D(self.x + b.x, self.y + b.y)
    
    def __sub__(self, b):
        return Vector2D(self.x - b.x, self.y - b.y)
    
    def __mul__(self, b):
        if type(b) == type(1.0):
            return Vector2D(self.x * b, self.y * b)
        raise "Can't do that yet"
    
    def __div__ (self, b):
        return Vector2D(self.x / b.x, self.y / b.y)
    
    def __abs__(self):
        return (abs(self.x), abs(self.y))
    
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalized(self):
        m = self.magnitude()
        return Vector2D(self.x / m, self.y / m)
    
    def copy(self):
        return Vector2D(self.x, self.y)
    
    def get(self):
        return (self.x, self.y)