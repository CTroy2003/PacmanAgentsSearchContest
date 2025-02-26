# PacmanAlgorithms

This was submitted as part of a competition against other coders where agents were scored under the following conditions:
+10 per pellet eaten
+500 for eating all pellets
-0.4 for each action by a pacman agent
-1*(compute time for next action [seconds])*1000
+100 for each agent

Files of Note -- 

My Aproach For class myAgent() --> First we sort all the remaining food dots to our agent by their manhattan distance, for each dot, we then search for the closest unclaimed food pellet. If another agent is closer to a pellet we ignore it and if all pellets are claimed we choose the closest pellet anyways. We then use Breadth First Search to get a path (which is returned as an array) to our target pellet, we pop the current move and return it. After this initial target is found, and a path to it is initialized, we can just check if the target pellet is still present instead of recomputing the whole segment above. If we look at this algorithm using amortized analysis this stored path significantly reduces our compute time to a fraction of before.

myAgents.py - We use search algorithms from search.py to construct pacman agent/s that work together to maximize score (eat as many pellets as possible) under different time, agent, and layout constraints.

My Aproach For class myAgent() --> 

search.py - In this file we implement different search algorithms for finding the path to a pellet. We implement algorithms such as DepthFirstSearch, BreadthFirstSearch, UniformCostSearch, and AStarSearch

To help you understand myAgents.py & search.py it might be helpful to look at game.py, pacman.py, and util.py.

Here are some useful commands --

To run a game with our myAgent -  
python pacman.py --pacman myAgents.py

To run myAgent on a single test - 
python pacman.py --layout test1.lay

To evaluate over all layouts - 
python autograder.py --pacman myAgents.py



