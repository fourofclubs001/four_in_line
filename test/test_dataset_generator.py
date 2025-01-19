import unittest
from src.FourInLine import *
from src.DatasetGenerator import *

class TestDatasetGenerator(unittest.TestCase):

    def test_can_play_random_game(self):

        game = FourInLine(5, 5)

        datasetGenerator = DatasetGenerator(game)

        self.assertFalse(game.isOver())

        datasetGenerator.playRandomGame()

        self.assertTrue(game.isOver())