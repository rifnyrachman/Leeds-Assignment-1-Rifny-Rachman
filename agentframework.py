"""
Created on Fri Oct  7 04:41:45 2022

@author: rifny
"""

#class, defining agents as abstract data type
import random

class Agent():
    def __init__(self,environment):
        self.store = 0
        self.environment = environment
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        
    def __str__(self):
        return "store = " + str(self.store) + " position(x y) :" + str(self.x) + " " + str(self.y)
    
    def move(self):
        if random.random()<0.5:
            self.x = (self.x+1)%100
        else:
            self.x = (self.x-1)%100
        if random.random()<0.5:
            self.y = (self.y+1)%100
        else:
            self.y = (self.y-1)%100
    
    # can you make it eat what is left?
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0