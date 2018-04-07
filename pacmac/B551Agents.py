from util import manhattanDistance
from game import Directions
import random, util
import pdb
from game import Agent

class B551Agent(Agent):
    def getAction(self, gameState):

        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):

        oldFood = currentGameState.getFood();
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        totalScore=0.0
        for ghost in newGhostStates:
          d=manhattanDistance(ghost.getPosition(), newPos)
          factor=1
          if(d<=1):
            if(ghost.scaredTimer!=0):
              factor=-1
              totalScore+=2000
            else:
              totalScore-=200

        for capsule in currentGameState.getCapsules():
          d=manhattanDistance(capsule,newPos)
          if(d==0):
            totalScore+=100
          else:
            totalScore+=10.0/d
          

        for x in range(oldFood.width):
          for y in range(oldFood.height):
            if(oldFood[x][y]):
              d=manhattanDistance((x,y),newPos)
              if(d==0):
                totalScore+=100
              else:
                totalScore+=1.0/(d*d)
        return totalScore
