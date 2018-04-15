from util import manhattanDistance
from game import Directions
import random, util
import pdb
from game import Agent

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
        #print chosenIndex
        #print legalMoves[chosenIndex]
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
        newCapsules=successorGameState.getCapsules()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        #print newPos
        #print newGhostStates[0]
        "*** YOUR CODE HERE ***"
        foodPos = newFood.asList()
        foodCount = len(foodPos)
        closestDistance = 1e6
        for i in range(foodCount):
          distance = manhattanDistance(foodPos[i],newPos) + foodCount*100
          if distance < closestDistance:
            closestDistance = distance
            closestFood = foodPos
        if foodCount == 0 :
          closestDistance = 0
        score = -closestDistance

        for ghost in newGhostStates:
          disGhost = manhattanDistance(newPos, ghost.getPosition())
          if ghost.scaredTimer > 0:
            score += 4*pow(max(8 - disGhost, 0), 2)
            #score +=30*1e6
          elif disGhost<=1:
            score-=4*pow(max(8 - disGhost, 0), 2)
            #score -=20*1e6
          else:
            score -= 2*pow(max(8 - disGhost, 0), 2)
            #score -=10*1e6
			
        disFood=[]
        for food in foodPos:
          disFood.append(1.0/manhattanDistance(newPos, food))
        if len(disFood)>0:
          score +=max(disFood)
		  
        disCapsule=[]
        for cap in newCapsules:
          disCapsule.append(50.0/manhattanDistance(newPos, cap))
        if len(disCapsule)>0:
          score +=max(disCapsule)
		  
		  


        return score #successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()