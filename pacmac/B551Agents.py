from util import manhattanDistance
from game import Directions
from game import Agent
import random, util

class B551Agent(Agent):
    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        if successorGameState.isWin():
            return float("inf") - 20
        ghostposition = currentGameState.getGhostPosition(1) 
        distfromghost = util.manhattanDistance(ghostposition, newPos) 
        score = max(distfromghost, 3) + successorGameState.getScore() 
        foodlist = newFood.asList() 
        closestfood = 100 
        for foodpos in foodlist: 
            thisdist = util.manhattanDistance(foodpos, newPos) 
            if (thisdist < closestfood): 
                closestfood = thisdist 
        if (currentGameState.getNumFood() > successorGameState.getNumFood()): 
            score += 100 
        if action == Directions.STOP: 
            score -= 3 
        score -= 3 * closestfood 
        capsuleplaces = currentGameState.getCapsules() 
        if successorGameState.getPacmanPosition() in capsuleplaces: 
            score += 120 
        return score 
