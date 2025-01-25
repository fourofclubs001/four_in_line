import unittest

from src.DatasetGenerator import *

class TestDatasetSaver(unittest.TestCase):

    def test_can_save_board_as_image_with_each_player_chips_on_different_channel(self):

        moves = [0,1,0,1,0,1,0]

        datasetGenerator = DatasetGenerator(5,5,iter(moves))

        datasetSaver = DatasetSaver(datasetGenerator, "dataset")

        datasetSaver.save(4)