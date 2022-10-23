"""
Created on Fri Oct  7 04:41:45 2022

@author: rifny
"""

import random

#class, defining agents as an abstract data type
class Agent():
    #initiating the variables in Agent class
    def __init__(self,i,agents,environment,y,x):
        self.store = 0
        self.i = i
        self.agents = agents
        self.environment = environment
        self.x = x
        self.y = y
        # self.x = random.randint(0,99) #uncomment to generate random number
        # self.y = random.randint(0,99)
    
    #bypass the agents function to return string as follows    
    def __str__(self):
        return "agent-" + str(self.i) + " ,store = " + str(self.store) \
            + " ,position(x y) :" + str(self.x) + " " + str(self.y)
            
    #create fucntion to move agents
    def move(self):
        #Agents move randomly by a step
        if random.random()<0.5:
            self.x = (self.x+1)%100 #any value more than 100 would be subtracted by 100
        else:
            self.x = (self.x-1)%100
        if random.random()<0.5:
            self.y = (self.y+1)%100
        else:
            self.y = (self.y-1)%100
            
        #Agents move quicker (by +/-5 steps) if they have more resources (>60)
        if self.store > 60:
            if random.random()<0.5:
                self.x = (self.x+5)%100 #make sure value is no more than 100
            else:
                self.x = (self.x-5)%100
            if random.random()<0.5:
                self.y = (self.y+5)%100
            else:
                self.y = (self.y-5)%100            

    
    # agents eat from the environment to add their stores
    def eat(self):
        #each agent eats 10 from the environment
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        #in case environment stores is less then 10, it prevents negative value
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
            
        #agents get sick if they have eaten more than 100, then throw all stores up
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
        
    #create function to calculate distance between the agent and another agent
    def distance_between(self,agents_row_b):
        return ((self.x-agents_row_b.x)**2+(self.y-agents_row_b.y)**2)**0.5
            
    #create function to share agent's store with its neighbour
    def share_with_neighbourhoods(self,neighbourhood):
        for i in range(len(self.agents)):
            distance = self.distance_between(self.agents[i])
            #each agent equally shares the store with its neighbour
            if (distance <= neighbourhood):
                ave = (self.agents[i].store + self.store)/2
                self.agents[i].store = ave
                self.store = ave
                #uncomment below code to see how much each agent shares to its neighbour
                #print("Agent-", i, "sharing: ", ave, ", distance: ",distance)
            else:
                pass
                
            #agent steals more resources from others if they are low
            if (self.store < 40) and (self.agents[i].store > 40):
                self.store += 20
                self.agents[i].store -= 20
                
    def wolves(self,wolf_x,wolf_y):
        #calculate agent's distance with the wolf
        wolf_dist = ((wolf_x-self.x)**2+(wolf_y-self.y)**2)**0.5
        if (wolf_dist < 50): #wolf eats agent if the distance is less than 50
            print("eaten by wolf")
            del self.agents # to delete eaten agents from agents list
            self.store = -99 #as a penalty in case del function does not work
            self.x = 0
            self.y = 0
            
        else: 
            print(self, ", Dstnc with wolf:", round(wolf_dist,2))
