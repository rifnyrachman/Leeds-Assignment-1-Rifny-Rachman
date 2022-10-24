"""
Created on Wed Sep 28 17:54:26 2022

@author: rifny rachman
Version: 1.0

ABOUT: This program is an agents-based model, which simulates some agents
behaviours and interactions. A simple Graphical User Interface is created to
enable users access the features easily.
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
import requests
import bs4
import numpy as np

#calculate processed time
start = time.process_time()

#setting the random seed for reproducability
random.seed(0)

#scraping the website and get html data to define agent's positions
r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html',
                 verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"}) #get y-column from table
td_xs = soup.find_all(attrs={"class" : "x"})  #get x-column from table
#print(td_ys) #uncomment to print y-column
#print(td_xs) #uncomment to print x-column

#creating environment for the agents
#reading data file for the environment
environment=[]  #initiate environment list
with open('in.txt', newline='') as f:
    dataset = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)  #read csv file
    for row in dataset:
        rowlist=[]
        for value in row:
            #print(value) #uncomment to print file
            rowlist.append(value)
        environment.append(rowlist)  #add environment list

#initiate agent list setup
agents=[]  #initiate agents list
num_of_agents = 30  #define starting number of agents
num_of_iterations = 100  #define default number of iterations
neighbourhood = 20  #define neighbourhood distance range

fig = matplotlib.pyplot.figure(figsize=(7, 7)) #initiate animation
ax = fig.add_axes([0, 0, 1, 1])

#Generate each agent's position within agent list using iteration
#Agent's positions is based on the html data
for i in range(num_of_agents):
    #in case the number of agents is more than what is provided in html data,
    #it generates random number for the rest
    if (i in range(len(td_xs))):
        x = int(td_xs[i].text)
    else:
        x = random.randint(0,99)
    if (i in range(len(td_ys))):        
        y = int(td_ys[i].text)
    else:
        y = random.randint(0,99)
    #add generated value from html file to agents list
    agents.append(agentframework.Agent(i,agents,environment,y,x))

#create agents status function    
def status():    
    print("\n===============================================\nAgents' Status:\n===============================================\n")
    for i in range(len(agents)):  
        if (agents[i].store >= 0):
            print(agents[i])
        else:
            pass
        
    store = [] #initiate store list to calculate statistic data
    for i in range(len(agents)):
        if (agents[i].store>=0):
            store.append(agents[i].store)
    #show agents store statistics summary
    store_mean = np.mean(store)
    store_std = np.std(store)
    print("\nSTATISTICS SUMMARY: \nStore Mean: ", round(store_mean,2))
    print("Store St Dev: ", round(store_std,2))
    print("Max Store: ", round(max(store),2))
    print("Min Store: ", round(min(store),2))

#create 3D Visualisation       
def visual_agents():
    fig = plt.figure()  #visualisation setup
    ax = fig.add_subplot(projection = '3d')
    
    #Mentioning all the three different axes
    x = [] #initiate variable list
    y = []
    z = []
    #define variable list
    for i in range(len(agents)):
        x.append(agents[i].x)
        y.append(agents[i].y)
        z.append(agents[i].store)
    #create array
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    # print(x,y,z)  #uncomment to check list, variable type and shape
    # print(type(x),type(y),type(z))
    # print(len(x),len(y),len(z)) 
    ax.scatter(x, y, z)  #create scatter plot
    ax.set_xlabel('agent-x')  #define label
    ax.set_ylabel('agent-y')
    ax.set_zlabel('store')
    plt.show()    #print the chart
    
#create agents shuffled status function
def shuffle_agents():
    print("\n===============================================\nShuffled Agents' Status:\n===============================================\n")
    random.shuffle(agents)  #shuffle agents list
    for i in range(len(agents)):
        print(agents[i])
    
#Test the communication between agents by printing agent-1 from agent-0
def com_test():
    print("\n===============================================\nCommunication test:\nCalling from agent-0:\n===============================================\n ",
          agents[0].agents[1])  #calling agent-1 from agent-0

#Create distance function    
def print_distance():
    dist=[] #create distance list to enable distance statistics summary
    print("\n===============================================\nDistances Between 2 Agents:\n===============================================\n")
    for i in range(len(agents)):
        for j in range(len(agents)):
            if (i!=j and i<j) and (agents[i].store >= 0):  #avoid distance printing redundancy
                distance_between = ((agents[i].x-agents[j].x)**2+(agents[i].y-agents[j].y)**2)**0.5
                print("agent-",i,"and agent-",j,"is:",round(distance_between,2))
                dist.append(distance_between)
            else:
                pass
    
    #show distance statistics summary
    dist_mean = np.mean(dist)
    dist_std = np.std(dist)
    print("\nSTATISTICS SUMMARY: \nDistance Mean: ", round(dist_mean,2))
    print("Distance St Dev: ", round(dist_std,2))
    print("max distance:",round(max(dist),2))
    print("min distance:",round(min(dist),2))

#create animation function to attach in GUI "Run Model" button
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function,
                                                   repeat=False)
    canvas.draw()
    
#Creating iteration function for animation
carry_on = True	
def update(frame_number):
    print("\n =========Agent's position at iteration-", frame_number,"=========")
    fig.clear()
    global carry_on
    
    #Create function that reflects agents behaviour
    for i in range(len(agents)):
        #Creating iteration stopping condition when agent's store >= 80
        if agents[i].store < 80:
            agents[i].move()  #move the agents
            agents[i].eat()  #agents eat from environment
            agents[i].share_with_neighbourhoods(neighbourhood)  #share store
            #print agents' position per iteration
            print("agent-" + str(i) + " ,store = " + str(round(agents[i].store,2)) \
                + " ,position(x y) :" + str(agents[i].x) + " " + str(agents[i].y))    
        else:
            carry_on = False
            
    #Uncomment to create random stopping condition
    # if random.random() < 0.1:
    #     carry_on = False
    #     print("stopping condition")

    #create visualisation
    plt.xlim(0,99)  #set axis range
    plt.ylim(0,99)
    plt.imshow(environment)
    for i in range(len(agents)):
        plt.scatter(agents[i].x,agents[i].y)  #create scatter plot
    #plt.show()
    canvas.draw()
    
    #print stopping condition
    if agents[i].store >= 80:
        print("\n ///////Stopping Condition at frame-", frame_number,"///////")
    else:
        pass
    
#Create frames for animation
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 20) & (carry_on) :
        yield a		
        a = a + 1

#Create function for wolves that eat some nearest sheeps (agents)        
def print_wolves():
    print("\n===============================================\nAdding Wolves\n===============================================\n")
    wolf_x=random.randint(0,99) #generate random wolf position
    wolf_y=random.randint(0,99)
    print("Wolf's position (x y) : ",wolf_x,wolf_y)
    for i in range(len(agents)):
        agents[i].wolves(wolf_x,wolf_y)  #get agents eaten by a wolf

#Create function that allows agents' breeding            
def breed():
  status()
  print("===============================================\nBreeding Agents\n===============================================")
  print("Additional agents after breeding:")
  for i in range(len(agents),(len(agents)+20)): #create additional 20 agents
      x = random.randint(0,99) #generate random agents position
      y = random.randint(0,99)
      agents.append(agentframework.Agent(i,agents,environment,y,x))
      #Add new agents' behaviour
      if agents[i].store < 80:  #condition of behaviour iteration
          agents[i].move()
          agents[i].eat()
          agents[i].share_with_neighbourhoods(neighbourhood)
      print(agents[i])        
        
#Create a csv file as an output from the program
with open('dataout.csv', 'w', newline='') as f2:
    writer = csv.writer(f2, delimiter=',')     
    for row in environment:        
        writer.writerow(row) # List of values.
        
#Create GUI
root = tkinter.Tk() #create window
root.wm_title("Welcome to Agent Based Modelling! ^^")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)  #initiate dropdown menu
agents_menu = tkinter.Menu(menu)
menu.add_cascade(label="Agents", menu=agents_menu)  #add main menu
agents_menu.add_command(label="Status", command=status)  #add submenu
agents_menu.add_command(label="Shuffled status", command=shuffle_agents)
agents_menu.add_command(label="Distance", command=print_distance) 
agents_menu.add_command(label="Communication Test", command=com_test)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run Model", command=run)  
model_menu.add_command(label="Add A Wolf", command=print_wolves) 
model_menu.add_command(label="Breed Agents", command=breed)
menu.add_cascade(label="3D Visualisation", command=visual_agents)

end = time.process_time()
print("=====================================")
print("INITIAL SETUP:\nnum_of_agents = 30\nnum_of_iterations = 100\nneighbourhood = 20\nprocessing time:",
      str(end-start),"\n=====================================")

tkinter.mainloop()