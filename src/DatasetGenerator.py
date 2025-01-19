import numpy as np
from src.FourInLine import *

class DatasetGenerator:

    def __init__(self, game: FourInLine):

        self.game = game

    def playRandomGame(self):

        while not self.game.isOver():

            noFullColumns = [column for column in range(self.game.width) if not self.game.isColumnFull(column)]
            randomColumn = np.random.choice(noFullColumns)
            self.game.insertAt(randomColumn)