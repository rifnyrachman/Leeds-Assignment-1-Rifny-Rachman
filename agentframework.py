"""
Created on Fri Oct  7 04:41:45 2022

@author: rifny
"""

#class, defining agents as abstract data type
import random

class Agent():
    def __init__(self,i,agents,environment,y,x):
        self.store = 0
        self.i = i
        self.agents = agents
        self.environment = environment
        self.x = x
        self.y = y
        # self.x = random.randint(0,99)
        # self.y = random.randint(0,99)
        
    # def __str__(self):
    #     return "agent-" + str(self.i) + " ,store = " + str(self.store) \
    #         + " ,position(x y) :" + str(self.x) + " " + str(self.y)
    
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
            
    def distance_between(self,agents_row_b):
        return ((self.x-agents_row_b.x)**2+(self.y-agents_row_b.y)**2)**0.5
            
    def share_with_neighbourhoods(self,neighbourhood):
        for i in range(len(self.agents)):
            distance = self.distance_between(self.agents[i])
            if distance <= neighbourhood:
                ave = (self.agents[i].store + self.store)/2
                self.agents[i].store = ave
                self.store = ave
                #activate below code to see how much each agent shares to its neighbour
                #print("Agent-", i, "sharing: ", ave, ", distance: ",distance)