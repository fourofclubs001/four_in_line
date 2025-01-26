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

        if not os.path.exists(self.datasetDirectoryName):

            os.mkdir(self.datasetDirectoryName)

        boards = self.datasetGenerator.getWinnerBoardHistory()

        for idx in range(len(boards)):

            boardRGBArray = self.convertToRGBArray(boards[idx])
            boardImage = Image.fromarray(boardRGBArray.astype(np.uint8))

            boardImage.save(os.path.join(self.datasetDirectoryName, f"board_{idx}.png"))