# Simulation of the Peter principle without learning

## An agent based simulation showing the effects of the Peter principle in a hierarchical structure

The Peter principle says that 

"The members of an organization climb the hierarchy until the level of maximum incompetence."

which means that inside a hierarchycal organization an agent will be promoted until he is not capable enough at the job to be promoted again.

This project simulates a company with employers with random generated age and competence filling 6 different levels in the hierarchycal structure.
The purpose of the simulation is to measure how the efficiency of the hierarchycal structure changes with different promotion strategies following different hypotheses on how the competence of the agents changes when promoted.

First we hire the agents randomly assining then an age and a competence.
The agents will be dismissed if the competence falls bellow 4.0 or the age is greater than 65.
If there is room in the upper level, an agent will be promoted following one of 3 different strategies: promoting the most competent, the least competent or a random agent.
When promoted the competence of the agent will be modified following one of two hypotheses: the Peter principle (in which will be randomly generated a new competence), or following the common sense (in which the competence will vary by 10%).
After the dismissing and promoting of the agents, they will age 1 year and the levels will be filled again with new agents.
This dinamic will play for a set number of iterations and a set number of executions.
At the end you can take the mean of the executions so you have a more smooth curve.

## How to run the simulation

First you need to make the directories where the data will be stored.
The directory 'data' contains two shell scripts.
The make_folders.sh creates the folders in which the output files of the program will be saved.
In case you want to delete the folders you can run the clear_folders.sh.

To run any of the scripts just type in the terminal:

> ./make_folders.sh
> ./clear_folders.sh

Once the folders are setup we can setup the parameters of our simulation.
In the file 'config.py' inside the 'peter' directory you can modify the hypothesis and the strategy used, as well as the number of iterations and executions.
For the hypothesis variable you can set it to 'peter' to follow the Peter principle or 'common' to follow the common sense hypothesis.
For the promotion strategy you can use 'best', 'worst' or 'random' to promote the most competent, the least competent and a random employee, respectively.

Then you can run the simulation at your will with:

> python3 main.py

Suppose you selected 'peter' and 'best' for your hypothesis and strategy, the output files will be saved in the './data/peter/best/output/' directory.
You can take the mean of the output files running the 'mean.sh' script.

> ./mean.sh

If you want to run all different combinations of hypotheses and strategies just run, after setting up the data folders, just run the 'run_all.sh' script:

> ./run_all.sh

