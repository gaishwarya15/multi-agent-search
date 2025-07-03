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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #start state of packman
    node=problem.getStartState()
    if(problem.isGoalState(node)):
        return []
    #DFS uses Stack as its data structure
    frontier=util.Stack()
    #start state and path i.e., empty list is added to the Stack(frontier)
    frontier.push((node,[]))
    explored=set()
    path=[]
    while(frontier.isEmpty()!=True):
        node,path=frontier.pop()
        #if node is already explored we go to next element in Stack
        if(node in explored):
            continue
        explored.add(node)
        #checks if pacman position is goal, if true returns path
        if(problem.isGoalState(node)):
            return path
        successors=problem.getSuccessors(node)
        for state,action,cost in successors :
            #cost is not considered as we donot use it in DFS
            #pacman new position and path is added to the Stack
            frontier.push((state,path+[action]))
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Artificial Intelligence-A Modern Approach-Third Edition by Stuart Russell and Peter Norvig.In this book page 82, a part of BFS Pseudocode is used as a reference.
    #start state of packman
    node=problem.getStartState()
    if(problem.isGoalState(node)):
        return []
    #BFS uses Queue as its data structure
    frontier=util.Queue()
    #start state and path i.e., empty list is added to the queue(frontier)
    frontier.push((node,[]))
    explored=set()
    while(frontier.isEmpty()!=True) :
        node,path=frontier.pop()
        #if node is already explored we go to next element in queue
        if(node in explored):
            continue
        explored.add(node)
        #checks if pacman position is goal, if true returns path
        if(problem.isGoalState(node)):
            return path
        successors=problem.getSuccessors(node)
        for state,action,cost in successors :
            #cost is not considered as we donot use it in BFS
            #pacman new position and path is added to the queue
            frontier.push((state,path+[action]))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #start state of packman
    node=problem.getStartState()
    if(problem.isGoalState(node)):
        return []
    #UCS uses Priority Queue as its data structure
    frontier=util.PriorityQueue()
    #start state, path i.e., empty list,cost and priority is added to the priority queue(frontier)
    frontier.push((node,[],0),0)
    explored=set()
    path=[]
    while(frontier.isEmpty()!=True):
        node,path,cost=frontier.pop()
        #if node is already explored we go to next element in priority queue
        if(node in explored):
            continue
        explored.add(node)
        #checks if pacman position is goal, if true returns path
        if(problem.isGoalState(node)):
            return path
        successors=problem.getSuccessors(node)
        for state,action,newcost in successors :
                #pacman new position and path is added to the priority queue
                #priority is given to lower cost
                priority=cost+newcost
                frontier.push((state,path+[action],cost+newcost),priority)
    return[]
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #start state of packman
    node=problem.getStartState()
    if(problem.isGoalState(node)):
        return []
    #A* search uses Priority Queue as its data structure
    frontier=util.PriorityQueue()
    #start state, path i.e., empty list,cost and priority is added to the priority queue(frontier)
    frontier.push((node,[],0),0)
    explored=set()
    path=[]
    while(frontier.isEmpty()!=True):
        node,path,cost=frontier.pop()
        #if node is already explored we go to next element in priority queue
        if(node in explored):
            continue
        explored.add(node)
        #checks if pacman position is goal, if true returns path
        if(problem.isGoalState(node)):
            return path
        successors=problem.getSuccessors(node)
        for state,action,newcost in successors :
                #pacman new position and path is added to the priority queue
                #A* search f(n)=g(n)+h(n) where g(n)=totalcost and h(n)=heuristic
                totalcost=cost+newcost
                frontier.push((state,path+[action],cost+newcost),totalcost+heuristic(state,problem))
    return[]
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
