"""
Created on Wed Sep 28 17:54:26 2022

@author: rifny

NOTE: Before running, to enable the pop-out animation type '%matplotlib qt'
in console window, then click enter. This is only needed once at the beginning.
"""

#import packages
import random
import matplotlib.pyplot as plt
import matplotlib.animation
import time
import agentframework
import csv
import matplotlib
matplotlib.use('TkAgg')
import tkinter

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

#create agent list
agents=[]
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

fig = matplotlib.pyplot.figure(figsize=(7, 7)) #initialize animation
ax = fig.add_axes([0, 0, 1, 1])

for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, agents, environment))
    print("agent-" + str(i) + " ,store = " + str(agents[i].store) \
        + " ,position(x y) :" + str(agents[i].x) + " " + str(agents[i].y))
    #print("Agent-",i,":",agents[i].x,agents[i].y)

#Test the communication by printing agent-1 from agent-0
print("Communicating test, calling from agent-0:\n",agents[0].agents[1].x,agents[0].agents[1].y)

#create animation function to attach in a button
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
#create distance function
def distance_between(agents_row_a,agents_row_b):
    return ((agents_row_a.x-agents_row_b.x)**2+(agents_row_a.y-agents_row_b.y)**2)**0.5

print("Agents Posistion After Random Movement:")

#Creating animation function
carry_on = True	
def update(frame_number):
    print("iteration", frame_number)
    fig.clear()
    global carry_on
    
#for j in range(num_of_iterations):
    #random.shuffle(agents) #shuffling the agents representation
    for i in range(num_of_agents):
        #set agents' behaviour
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbourhoods(neighbourhood)
        #print agents' position per iteration
        print("agent-" + str(i) + " ,store = " + str(round(agents[i].store,2)) \
            + " ,position(x y) :" + str(agents[i].x) + " " + str(agents[i].y))    
   
    #Creating random stopping condition
    # if random.random() < 0.1:
    #     carry_on = False
    #     print("stopping condition")
    
    #Creating stopping condition when agent's store > 80
    #Since the agent's store starts from 0 then increasing, it is better to set
    #stopping condition in ">" to allow some movement before stopping
    for i in range(num_of_agents):
        if agents[i].store > 80:
            carry_on = False
            print("Stopping Condition at frame-", frame_number)
        
    #create visualisation
    plt.xlim(0,99)
    plt.ylim(0,99)
    plt.imshow(environment)
    for i in range(num_of_agents):
        plt.scatter(agents[i].x,agents[i].y)
    #plt.show()
    canvas.draw()
    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
#calling animation module
# animation = matplotlib.animation.FuncAnimation(
#     fig, update, interval=1, repeat=False, frames=num_of_iterations)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

#print the latest agents' position
# for i in range(num_of_agents):  
#     print(agents[i])
        #print("Agent-",i,":",agents[i].x,agents[i].y)
    
#call the distance function for all agents
dist=[]
print("Distance Between 2 Agents:")
for i in range(num_of_agents):
    for j in range(num_of_agents):
        if i!=j and i<j:
            distance_between(agents[i],agents[j])
            print("agent-",i,"and agent-",j,"is:",round(distance_between(agents[i],agents[j]),2))
            dist.append(distance_between(agents[i],agents[j]))
        else:
            pass
    
#show max and min distances
print("max distance:",round(max(dist),2))
print("min distance:",round(min(dist),2))  
 
end = time.process_time()
print("time:",str(end-start))

with open('dataout.csv', 'w', newline='') as f2:
    writer = csv.writer(f2, delimiter=',')     
    for row in environment:        
        writer.writerow(row) # List of values.
        
#Create GUI
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)   
     
tkinter.mainloop()