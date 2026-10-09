# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Team assignment: Member 2 (Q1).

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first.

    Team assignment: Member 3 (Q2).
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first.

    Team assignment: Member 4 (Q3).
    """
    # Priority queue stores tuples of: (state, actions, accumulated_cost)
    # The queue priority is the accumulated path cost g(n)
    frontier = util.PriorityQueue()
    start_state = problem.getStartState()
    frontier.push((start_state, [], 0), 0)

    # Set to keep track of expanded states
    expanded = set()

    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()

        # Skip duplicate entries for states already expanded
        if state in expanded:
            continue

        # Check goal condition when state is popped (ensures optimal solution)
        if problem.isGoalState(state):
            return actions

        # Mark state as expanded
        expanded.add(state)

        # Generate and evaluate successors
        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in expanded:
                new_actions = actions + [action]
                new_cost = cost + step_cost
                frontier.push((successor, new_actions, new_cost), new_cost)

    # Return empty list if no path is found
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first.

    Team assignment: Member 1 (Q4).
    """
    "*** YOUR CODE HERE ***"
    frontier = PriorityQueue()
    start_state = problem.getStartState()
    
    # Item in queue: (current_state, action_list, path_cost_g)
    # Priority: f(n) = g(n) + h(n)
    initial_h = heuristic(start_state, problem)
    frontier.push((start_state, [], 0), initial_h)
    
    visited = {}  # state -> lowest g(n) to reach it

    while not frontier.isEmpty():
        state, actions, current_g = frontier.pop()

        if state in visited and visited[state] <= current_g:
            continue
        visited[state] = current_g

        if problem.isGoalState(state):
            return actions

        for next_state, action, step_cost in problem.getSuccessors(state):
            new_g = current_g + step_cost
            if next_state not in visited or visited[next_state] > new_g:
                f_cost = new_g + heuristic(next_state, problem)
                frontier.push((next_state, actions + [action], new_g), f_cost)

    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
