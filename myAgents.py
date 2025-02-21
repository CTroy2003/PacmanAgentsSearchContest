# myAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from game import Agent
from searchProblems import PositionSearchProblem

import util
import time
import search

"""
IMPORTANT
`agent` defines which agent you will use. By default, it is set to ClosestDotAgent,
but when you're ready to test your own agent, replace it with MyAgent
"""
def createAgents(num_pacmen, agent='MyAgent'):
    return [eval(agent)(index=i) for i in range(num_pacmen)]



class MyAgent(Agent):
   """
   A multi-agent Pac-Man that minimizes duplicate target pursuit by locally
   selecting the closest food dot that is not already "claimed" by a nearer agent.
   It caches a BFS path to its chosen target and only recalculates when necessary.
   """


   def getAction(self, state):
       """
       Returns the next action for this agent.
       If the current target is no longer available or if the cached path is empty,
       the agent selects a new target by examining available food dots and choosing
       one that no other agent is closer to. It then computes a BFS path to that target.
       Otherwise, it follows its cached path.
       """
       from search import breadthFirstSearch
       from searchProblems import PositionSearchProblem
       from game import Directions
       from util import manhattanDistance


       # Retrieve this agent's current position and the food grid.
       currentPos = state.getPacmanPosition(self.index)
       foodList = state.getFood().asList()
       numAgents = state.getNumPacmanAgents()


       # If no food remains, stop.
       if not foodList:
           return Directions.STOP


       # If our current target is no longer available or our cached path is nearly empty, choose a new target.
       if self.target not in foodList or not self.cachedPath:
           # Sort food dots by Manhattan distance from our current position.
           candidateDots = sorted(foodList, key=lambda dot: manhattanDistance(currentPos, dot))
           chosen = None


           # Loop through candidate dots (from closest onward).
           for dot in candidateDots:
               # Check if any other agent is closer to this dot.
               claimed = False
               for i in range(numAgents):
                   if i == self.index:
                       continue
                   otherPos = state.getPacmanPosition(i)
                   if manhattanDistance(otherPos, dot) < manhattanDistance(currentPos, dot):
                       claimed = True
                       break
               if not claimed:
                   chosen = dot
                   break


           # If all dots appear claimed, simply pick the closest.
           if chosen is None:
               chosen = candidateDots[0]


           self.target = chosen


           # Compute a BFS path from our current position to the chosen target.
           problem = PositionSearchProblem(state, self.index, costFn=lambda x: 1, goal=self.target, warn=False, visualize=False)
           self.cachedPath = breadthFirstSearch(problem)


       # Follow the cached path: return the next action.
       if self.cachedPath:
           return self.cachedPath.pop(0)
       else:
           return Directions.STOP


   def initialize(self):
       """
       Called when the agent is first created.
       Here, we initialize our local target and cached path.
       """
       self.target = None
       self.cachedPath = []
       self.path = []




"""
Put any other SearchProblems or search methods below. You may also import classes/methods in
search.py and searchProblems.py. (ClosestDotAgent as an example below)
"""

class ClosestDotAgent(Agent):

    def findPathToClosestDot(self, gameState):
        """
        Returns a path (a list of actions) to the closest dot, starting from
        gameState.
        """
        # Here are some useful elements of the startState
        startPosition = gameState.getPacmanPosition(self.index)
        food = gameState.getFood()
        walls = gameState.getWalls()
        problem = AnyFoodSearchProblem(gameState, self.index)


        "*** YOUR CODE HERE ***"
        from search import breadthFirstSearch
        return breadthFirstSearch(problem)
        util.raiseNotDefined()

    def getAction(self, state):
        return self.findPathToClosestDot(state)[0]

class AnyFoodSearchProblem(PositionSearchProblem):
    """
    A search problem for finding a path to any food.

    This search problem is just like the PositionSearchProblem, but has a
    different goal test, which you need to fill in below.  The state space and
    successor function do not need to be changed.

    The class definition above, AnyFoodSearchProblem(PositionSearchProblem),
    inherits the methods of the PositionSearchProblem.

    You can use this search problem to help you fill in the findPathToClosestDot
    method.
    """

    def __init__(self, gameState, agentIndex):
        "Stores information from the gameState.  You don't need to change this."
        # Store the food for later reference
        self.food = gameState.getFood()

        # Store info for the PositionSearchProblem (no need to change this)
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition(agentIndex)
        self.costFn = lambda x: 1
        self._visited, self._visitedlist, self._expanded = {}, [], 0 # DO NOT CHANGE

    def isGoalState(self, state):
        """
        The state is Pacman's position. Fill this in with a goal test that will
        complete the problem definition.
        """
        x,y = state

        "*** YOUR CODE HERE ***"
        return self.food[x][y]
        util.raiseNotDefined()

