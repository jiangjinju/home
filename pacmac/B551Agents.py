from util import manhattanDistance
from game import Directions
from game import Agent

class B551Agent(Agent):
    def getAction(self, gameState):
        legalMoves = gameState.getLegalActions()

        return legalMoves[0]
