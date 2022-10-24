# Agent-Based Modelling Program
This program is a simulation of multiple agents setup. Agents would be generated from web scraping, then the program lets them to interact, both with other agents and their environment. A Graphical User Interface has been generated to enable users intervene in the program setup, for example by adding wolves (predator agents), breeding agents, etc. An animated graphic is given when users are running the program, as well as the statistics, informative text output, and 3D Visualization.

## How to Install and Run This Program
### Before Installation
* Make sure you have any application to run Python (Spyder is recommended)
* Make sure you have a stable internet connection

### Installation
1. Download the whole files in this repository: code >> download zip
2. Unzip the downloaded folder
3. Open model.py and agentframework.py using Spyder

### Running This Program
1. Open model.py window
2. Run the program
3. Choose feature from the GUI
4. Graphical and animated output would pop up, while informative text (including statistics summary) would appear on the console window.

## Program Features
### Initiate this program
Once you run the program, it will show the GUI window and initial setup on console window:
![GUI Window](https://user-images.githubusercontent.com/113346710/197628239-eddb4579-dfed-40df-8b93-6b5a103c69c2.png)
![Initial Setup](https://user-images.githubusercontent.com/113346710/197627683-0bf6336d-2f29-41f0-8bf0-21931fba0f66.png)

There are some features you could choose in the menu or dropdown menu as follows:

![Agents dropdown menu](https://user-images.githubusercontent.com/113346710/197629007-e5c5a925-83ae-4c98-b5a6-0cecd971ca94.png)
![Model dropdown menu](https://user-images.githubusercontent.com/113346710/197631767-b1fcc8db-ca0e-4390-b591-c251e9842a92.png)

### Choosing Features
Below is the function of each feature:
* Status: to show updated living agents' store, positions, as well as statistics summary
* Shuffle status: to shuffle current living agents' representation
* Distance: to show current distance between 2 agents
* Communicaation test: to call another agent from a certain agent. This makes sure interaction between agents
* Run model: to apply iterated behaviour to the agents. This includes move the agents, eat from environment, and share store with neighbour. Along with the iteration, there will be a pop up animation to illustrate the agents movements.

*Note: Several behaviours have been modified, such us: agents movement is nimbler when they have more store, agents get sick (throw up all store) when they eat more than certain value, and agents steal from their neighbour when their store is getting low.
* Add a wolf: to add a predator agent that eat some closest agents.

*Note: Click multiple times to add more wolves
* Breed agents: to add new agents
* 3D Visualisation: to show the latest agents status in the 3D Graphical representation

### Limitation
While most of features allow re-run to get the most updated representation, only the animation feature from "Run model" could not be re-run.

## Further Documents
### Program Documentation
A documentation file while running this program is given in the documentation.word. This file could be a further guidance like user manual and a validation of the model.
### License
A license file is provided as a guideline for programmer fellows who are willing to use codes in this program.
