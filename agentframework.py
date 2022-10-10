# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 04:41:45 2022

@author: rifny
"""

#class, defining agents as abstract data type
import random

class Agent():
    def __init__(self):
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        print(self.x,self.y)
    
    def move(self):
        if random.random()<0.5:
            self.x = (self.x+1)%100
        else:
            self.x = (self.x-1)%100
        if random.random()<0.5:
            self.y = (self.y+1)%100
        else:
            self.y = (self.y-1)%100 