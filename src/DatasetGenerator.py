import numpy as np
from src.FourInLine import *

class CannotGetWinnerPropertyWhenThereIsNoWinner(Exception):

    def __init__(self):

        super().__init__("Can not get winner property when there is no winner")

class DatasetGenerator:

    def __init__(self, width: int, height: int, randomGenerator):

        self.width = width
        self.height = height

        self.game = FourInLine(self.width, self.height)
        self.randomGenerator = randomGenerator

        self.boardHistory = []
        self.moveHistory = []

        self.boardHistories = []
        self.moveHistories = []

    def restartIfGameIsOver(self):

        if self.game.isOver(): 
            
            self.game = FourInLine(self.width, self.height)
            self.boardHistory = []
            self.moveHistory = []

    def playRandomGame(self):

        self.restartIfGameIsOver()

        while not self.game.isOver():

            self.boardHistory.append(self.game.getBoard())

            noFullColumns = [column for column in range(self.game.width) if not self.game.isColumnFull(column)]

            if self.randomGenerator: randomColumn = next(self.randomGenerator)
            else: randomColumn = np.random.choice(noFullColumns)
            
            self.game.insertAt(randomColumn)
            self.moveHistory.append(randomColumn)

        self.boardHistory.append(self.game.getBoard())

    def playManyRandomGames(self, numberOfGames: int):

        for _ in range(numberOfGames):

            isATie = True

            while isATie:

                self.playRandomGame()
                isATie = self.game.isATie()
                
            self.boardHistories.append(self.getBoardHistory())
            self.moveHistories.append(self.getMoveHistory())

    def getBoardHistory(self):

        return self.boardHistory.copy()
    
    def getBoardHistories(self):

        return self.boardHistories.copy()
    
    def getMoveHistory(self):

        return self.moveHistory.copy()
    
    def getMoveHistories(self):

        return self.moveHistories.copy()

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

        return [self.moveHistory[idx] for idx in range(movesStart, len(self.moveHistory), 2)]