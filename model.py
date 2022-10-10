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

#setting the random seed for reproducability
random.seed(0)

#creating environment for the agents
#reading data file for the environment
environment=[]
with open('in.txt', newline='') as f:
    dataset = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist=[]
        for value in row:
            #print(value)
            rowlist.append(value)
        environment.append(rowlist)
        

'''
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
'''

#create agent list
agents=[]
num_of_agents = 10
num_of_iterations = 99
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))
    print(agents[i])
    #print("Agent-",i,":",agents[i].x,agents[i].y)
    
#create distance function
def distance_between(agents_row_a,agents_row_b):
    return ((agents_row_a.x-agents_row_b.x)**2+(agents_row_a.y-agents_row_b.y)**2)**0.5

#create random walk for num_of_iterations times
print("Agents Posistion After Random Movement:")
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

#print the latest agents' position
for i in range(num_of_agents):  
    print(agents[i])
    #print("Agent-",i,":",agents[i].x,agents[i].y)
    
    
#call the distance function for all agents
dist=[]
print("Distance Between 2 Agents")
for i in range(num_of_agents):
    for j in range(num_of_agents):
        if i!=j and i<j:
            distance_between(agents[i],agents[j])
            print("agent-",i,"and agent-",j,"is:",distance_between(agents[i],agents[j]))
            dist.append(distance_between(agents[i],agents[j]))
        else:
            pass
    
#show max and min distances
print("max distance:",max(dist))
print("min distance:",min(dist))  
 
#create visualisation
plt.xlim(0,99)
plt.ylim(0,99)
plt.imshow(environment)
for i in range(num_of_agents):
    plt.scatter(agents[i].x,agents[i].y)
plt.show()

end = time.process_time()
print("time:",str(end-start))

with open('dataout.csv', 'w', newline='') as f2:
    writer = csv.writer(f2, delimiter=',')     
    for row in environment:        
        writer.writerow(row) # List of values.