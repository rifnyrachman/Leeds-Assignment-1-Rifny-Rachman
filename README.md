# Agent-Based Modelling Program
(Word count: 580)

This program is a simulation of multiple agents set up. Agents would be generated from web scraping, and then the program lets them interact, both with other agents and their environment. A Graphical User Interface has been generated to enable users to intervene in the program setup, for example by adding wolves (predator agents), breeding agents, etc. An animated graphic is given when users are running the program, as well as the statistics, informative text output, and 3D Visualization.

## How to Install and Run This Program
### Before Installation
* Make sure you have an application to run Python (Spyder is recommended)
* Make sure you have a stable internet connection

### Installation
1. Download the whole files in this repository: code >> download zip
2. Unzip the downloaded folder. This folder contains:
* `model.py`: The main code source of this program that would be run to access the program functionality.
* `agentframework.py`: Another code source for agents that is employed in the main code source.
* `documentation.pdf`: Validation evidence as well as further user guidance to this program.
* `README.md`: This file, which is a brief description and main guidance about this program.
* `LICENSE.md`: A guidance to re-use or develop this program.
* `in.txt`: Data used for model's environment.
* `dataout.csv`: Printed out CSV file from the program.

3. Open `model.py` and `agentframework.py` using Spyder

### Setup Preparation (for Spyder)
Hit the following buttons:
1. _Tools_ button on top of window -> _Preferences_ -> _IPython Console_ -> _Graphics_
2. Set Backend to _Tkinter_, then click _OK_.

### Running This Program
1. Open the `model.py` window
2. _Run_ the program
3. Choose any feature from the GUI
4. Graphical and animated output would pop up, while informative text (including statistics summary) would appear on the console window.

## Program Features
### Initiate this program
Once you run the program, it will show the GUI window and initial setup on the console window:
![GUI Window](https://user-images.githubusercontent.com/113346710/197628239-eddb4579-dfed-40df-8b93-6b5a103c69c2.png)
![Initial Setup](https://user-images.githubusercontent.com/113346710/197627683-0bf6336d-2f29-41f0-8bf0-21931fba0f66.png)

There are some features you could choose in the menu or dropdown menu as follows:

![Agents dropdown menu](https://user-images.githubusercontent.com/113346710/197629007-e5c5a925-83ae-4c98-b5a6-0cecd971ca94.png)
![Model dropdown menu](https://user-images.githubusercontent.com/113346710/197631767-b1fcc8db-ca0e-4390-b591-c251e9842a92.png)

### Choosing Features
Below is the function of each feature:
* _Status_: to show updated living agents' store, positions, as well as statistics summary
* _Shuffle status_: to shuffle current living agents' representation
* _Distance_: to show the current distance between 2 agents
* _Communication test_: to call another agent from a certain agent. This makes sure interaction between agents
* _Run model_: to apply iterated behaviour to the agents. This includes moving the agents, eating from environment, and sharing the store with neighbours. Along with the iteration, there will be a pop up animation to illustrate the agents movements.

**Note**: Several behaviours have been modified, such as agents' movement is nimbler when they have more stores, agents get sick (throw up all stores) when they eat more than a certain value, and agents steal from their neighbours when their store is getting low.
* _Add a wolf_: to add a predator agent that eats some closest agents.

**Note**: Click multiple times to add more wolves
* _Breed agents_: to add new agents
* _3D Visualisation_: to show the latest agents' status in the 3D Graphical representation

### Limitation
While most of the features allow re-run to get the most updated representation, only the animation feature from "Run model" could not be re-run.

## Further Documents
### Program Documentation
A documentation file while running this program is given in the `documentation.pdf`. This file could be further guidance like user manual and validation of the model.
### License
The `LICENSE.md` file is provided as a guideline for programmer fellows who are willing to use codes in this program.
