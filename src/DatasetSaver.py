import os
from PIL import Image
from src.DatasetGenerator import *

class DatasetSaver:

    def __init__(self, datasetGenerator: DatasetGenerator, datasetDirectoryName: str):

        self.datasetGenerator = datasetGenerator
        self.datasetDirectoryName = datasetDirectoryName

    def convertToRGBArray(self, board: np.ndarray):

        boardRGBArray = np.zeros((board.shape[0], board.shape[1], 3))

        for row in range(len(board)):

            for column in range(len(board[row])):

                if board[row][column] == self.datasetGenerator.game.getWinner():

                    boardRGBArray[row, column, 0] = 255

                elif board[row][column] != EMPTY_PLACE:

                    boardRGBArray[row, column, 1] = 255

        return boardRGBArray

    def save(self, numberOfBoards: int):

        self.datasetGenerator.playRandomGame()

        board = np.repeat('O', 
                          (self.datasetGenerator.width*
                           self.datasetGenerator.height)).reshape((self.datasetGenerator.width, 
                                                                   self.datasetGenerator.height))
        
        boardRGBArray = self.convertToRGBArray(board)
        boardImage = Image.fromarray(boardRGBArray.astype(np.uint8))

        if not os.path.exists(self.datasetDirectoryName):

            os.mkdir(self.datasetDirectoryName)

        boardImage.save(os.path.join(self.datasetDirectoryName, "board_0.png"))