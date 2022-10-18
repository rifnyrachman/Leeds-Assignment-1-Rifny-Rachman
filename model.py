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
import requests
import bs4

#calculate processed time
start = time.process_time()

#setting the random seed for reproducability
random.seed(0)

#scraping the website and get html data to define agent's positions
r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys) #uncomment to print y column
#print(td_xs) #uncomment to print x column

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
num_of_agents = 30
num_of_iterations = 100
neighbourhood = 20

fig = matplotlib.pyplot.figure(figsize=(7, 7)) #initialize animation
ax = fig.add_axes([0, 0, 1, 1])

#Generate each agent's position within agent list using iteration
#Agent's positions is based on the html data
print("Agents' Initial Positions:")
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
    agents.append(agentframework.Agent(i,agents,environment,y,x))
    
    print("agent-" + str(i) + " ,store = " + str(agents[i].store) \
        + " ,position(x y) :" + str(agents[i].x) + " " + str(agents[i].y))
    #print("Agent-",i,":",agents[i].x,agents[i].y)

#random.shuffle(agents) #to shuffle the agents representation

#Test the communication between agents by printing agent-1 from agent-0
print("\n\nCommunicating test, calling from agent-0:\n",
      "agent-1 , position(x y): ",agents[0].agents[1].x,agents[0].agents[1].y)

#create animation function to attach in GUI "Run Model" button
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

#create distance function between two agents
def distance_between(agents_row_a,agents_row_b):
    return ((agents_row_a.x-agents_row_b.x)**2+(agents_row_a.y-agents_row_b.y)**2)**0.5


#Creating iteration function for animation
carry_on = True	
def update(frame_number):
    print("\n =========Agent's position at iteration-", frame_number,"=========")
    fig.clear()
    global carry_on
    
    for i in range(num_of_agents):
        #set agents' behaviour
        #Creating stopping condition when agent's store >= 80
        if agents[i].store < 80:
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbourhoods(neighbourhood)
            #print agents' position per iteration
            print("agent-" + str(i) + " ,store = " + str(round(agents[i].store,2)) \
                + " ,position(x y) :" + str(agents[i].x) + " " + str(agents[i].y))    
        else:
            carry_on = False
            
    #Creating random stopping condition
    # if random.random() < 0.1:
    #     carry_on = False
    #     print("stopping condition")

    #create visualisation
    plt.xlim(0,99)
    plt.ylim(0,99)
    plt.imshow(environment)
    for i in range(num_of_agents):
        plt.scatter(agents[i].x,agents[i].y)
    #plt.show()
    canvas.draw()
    
    if agents[i].store >= 80:
        print("\n ///////Stopping Condition at frame-", frame_number,"///////")
    else:
        pass
    
#Create frames for animation
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 20) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

#Create function for wolves that eat some nearest sheeps (agents)        
def wolves():
    print("===============================================\nAdding Wolves\n===============================================")
    wolf_x=random.randint(0,99)
    wolf_y=random.randint(0,99)
    print("Wolf's position (x y) : ",wolf_x,wolf_y)
    print("Remaining agents:")
    for i in range(num_of_agents):
        wolf_dist = ((wolf_x-agents[i].x)**2+(wolf_y-agents[i].y)**2)**0.5
        if (wolf_dist < 50):
            agents.remove(agents[i])
        else:       
            print("Agent-",i,", Distance with the wolf:", round(wolf_dist,2))

#Create function that allows agents' breeding            
def breed():
    print("===============================================\nBreeding Agents\n===============================================")
    print("Additional agents after breeding:")
    for i in range(30,51):
        x = random.randint(0,99)
        y = random.randint(0,99)
        agents.append(agentframework.Agent(i,agents,environment,y,x))
        print ("Agent-",i, ",store =",agents[i].store,",Position (x y) : ",agents[i].x,agents[i].y)
        num_of_agents == i
           
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
print("\n\nDistance Between 2 Agents:")
for i in range(num_of_agents):
    for j in range(num_of_agents):
        if i!=j and i<j:
            distance_between(agents[i],agents[j])
            print("agent-",i,"and agent-",j,"is:",round(distance_between(agents[i],agents[j]),2))
            dist.append(distance_between(agents[i],agents[j]))
        else:
            pass
    
#show max and min distances
print("\nmax distance:",round(max(dist),2))
print("min distance:",round(min(dist),2))  
 
end = time.process_time()
print("\nprocessing time:",str(end-start))

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
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run Model", command=run)  
model_menu.add_command(label="Add A Wolf", command=wolves)  #additional button
model_menu.add_command(label="Breed Agents", command=breed) #additional button 

tkinter.mainloop()