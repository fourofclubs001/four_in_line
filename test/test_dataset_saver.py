import unittest
from PIL import Image
from src.FourInLine import *
from src.DatasetGenerator import *
from src.DatasetSaver import *

class TestDatasetSaver(unittest.TestCase):

    def setUp(self):

        self.width = 5
        self.height = 5

        self.moves = [0,1,0,1,0,1,0]

        self.datasetGenerator = DatasetGenerator(self.width, self.height, iter(self.moves))
        self.datasetSaver = DatasetSaver(self.datasetGenerator, "dataset")


    def test_can_convert_game_empty_board_to_image_value(self):

        boardRGBArray = self.datasetSaver.convertToRGBArray(self.datasetGenerator.game.getBoard())

        self.assertTrue(np.array_equal(boardRGBArray, np.zeros((5,5,3))))

    def test_can_convert_winning_chip_to_image_values_on_first_channel(self):

        self.datasetGenerator.playRandomGame()

        oneWinnerChip = self.datasetGenerator.getBoardHistory()[1]

        boardRGBArray = self.datasetSaver.convertToRGBArray(oneWinnerChip)
        winnerChannel = boardRGBArray[:,:,0]

        expected = np.zeros((self.width, self.height))
        expected[0,0] = 255

        self.assertTrue(np.array_equal(winnerChannel, expected))

    def test_can_convert_loser_chip_to_image_values_on_second_channel(self):

        self.datasetGenerator.playRandomGame()

        oneLoserChip = self.datasetGenerator.getBoardHistory()[2]

        boardRGBArray = self.datasetSaver.convertToRGBArray(oneLoserChip)
        loserChannel = boardRGBArray[:,:,1]

        expected = np.zeros((self.width, self.height))
        expected[0,1] = 255

        self.assertTrue(np.array_equal(loserChannel, expected))

    def test_can_convert_game_board_to_image_value_with_many_winner_and_loser_cihps(self):

        self.datasetGenerator.playRandomGame()

        board = self.datasetGenerator.getBoardHistory()[-1]

        boardRGBArray = self.datasetSaver.convertToRGBArray(board)
        winnerChannel = boardRGBArray[:,:,0]
        loserChannel = boardRGBArray[:,:,1]
        emptyChannel = boardRGBArray[:,:,2]

        expectedWinnerChannel = np.zeros((self.width, self.height))
        expectedWinnerChannel[0:4,0] = 255

        expectedLoserChannel = np.zeros((self.width, self.height))
        expectedLoserChannel[0:3,1] = 255

        expectedEmptyChannel = np.zeros((self.width, self.height))

        self.assertTrue(np.array_equal(winnerChannel, expectedWinnerChannel))
        self.assertTrue(np.array_equal(loserChannel, expectedLoserChannel))
        self.assertTrue(np.array_equal(emptyChannel, expectedEmptyChannel))

    def test_can_save_board_as_image_with_each_player_chips_on_different_channel(self):

        moves = [0,1,0,1,0,1,0]

        datasetGenerator = DatasetGenerator(5,5,iter(moves))

        datasetSaver = DatasetSaver(datasetGenerator, "dataset")

        datasetSaver.save(1)

        image = Image.open("dataset/board_0.png")
        image_array = np.array(image)

        self.assertTrue(np.array_equal(image_array, datasetGenerator.getBoardHistory()[0]))