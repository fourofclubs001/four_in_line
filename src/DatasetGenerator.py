import numpy as np
from src.FourInLine import *

class CannotGetWinnerPropertyWhenThereIsNoWinner(Exception):

    def __init__(self):

        super().__init__("Can not get winner property when there is no winner")

class DatasetGenerator:

    def __init__(self, width: int, height: int, randomGenerator):

        self.game = FourInLine(width, height)
        self.randomGenerator = randomGenerator

        self.boardHistory = []
        self.moves = []

    def playRandomGame(self):

        while not self.game.isOver():

            self.boardHistory.append(self.game.getBoard())

            noFullColumns = [column for column in range(self.game.width) if not self.game.isColumnFull(column)]

            if self.randomGenerator: randomColumn = next(self.randomGenerator)
            else: randomColumn = np.random.choice(noFullColumns)
            
            self.game.insertAt(randomColumn)
            self.moves.append(randomColumn)

        self.boardHistory.append(self.game.getBoard())

    def getBoardHistory(self):

        return self.boardHistory
    
    def getMoves(self):

        return self.moves
    
    def assertThereIsAWinner(self):

        isThereAWinner = self.game.isThereAWinner()

        if not isThereAWinner: raise CannotGetWinnerPropertyWhenThereIsNoWinner

    def getWinnerBoardHistory(self):

        self.assertThereIsAWinner()

        if self.game.getWinner() == BLUE_CHIP: historyStart = 0
        else: historyStart = 1

        return [self.boardHistory[idx] for idx in range(historyStart, len(self.boardHistory), 2)]
    
    def getWinnerMoves(self):

        if self.game.getWinner() == BLUE_CHIP: movesStart = 0
        else: movesStart = 1

        return [self.moves[idx] for idx in range(movesStart, len(self.moves), 2)]