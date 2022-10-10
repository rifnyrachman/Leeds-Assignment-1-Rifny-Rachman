# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 17:54:26 2022

@author: rifny
"""

#import packages
import random
import matplotlib.pyplot as plt
import time
import agentframework
import csv

#calculate processed time
start = time.process_time()

#creating environment for the agents
#reading data file for the environment
f = open("in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
print(environment)
f.close()

#create data visualization for the environment
plt.imshow(environment)
plt.show()


#create agent list
agents=[]
num_of_agents = 10
num_of_iterations = 100
for i in range(num_of_agents):
    print("Agent-",i,":")
    agents.append(agentframework.Agent())
    
#create distance function
def distance_between(agents_row_a,agents_row_b):
    return ((agents_row_a.x-agents_row_b.x)**2+(agents_row_a.y-agents_row_b.y)**2)**0.5

#create random walk for num_of_iterations times
print("Agents Posistion After Random Movement:")
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

#print the latest agents' position
for i in range(num_of_agents):  
    print("Agent-",i,":",agents[i].x,agents[i].y)
    
    
#call the distance function for all agents
dist=[]
for i in range(num_of_agents):
    for j in range(num_of_agents):
        if i!=j and i<j:
            distance_between(agents[i],agents[j])
            print("distance between agent-",i,"and agent-",j,"is:",distance_between(agents[i],agents[j]))
            dist.append(distance_between(agents[i],agents[j]))
        else:
            pass
    
#show max and min distances
print("max distance:",max(dist))
print("min distance:",min(dist))  
 
#create visualisation
plt.xlim(0,99)
plt.ylim(0,99)
for i in range(num_of_agents):
    plt.scatter(agents[i].x,agents[i].y,c="blue")
plt.show()

end = time.process_time()
print("time:",str(end-start))