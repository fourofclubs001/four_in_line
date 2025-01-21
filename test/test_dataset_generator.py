import unittest
from src.FourInLine import *
from src.DatasetGenerator import *

class TestDatasetGenerator(unittest.TestCase):

    def setUp(self):

        self.blueWinMoves = [0,1,0,1,0,1,0]
        self.redWinMoves = [0,1,0,1,0,1,2,1]
        randomGenerator = iter(self.blueWinMoves)

        self.width = 5
        self.height = 5

        self.datasetGenerator = DatasetGenerator(self.width, self.height, randomGenerator)

    def test_can_play_random_game(self):

        self.assertFalse(self.datasetGenerator.game.isOver())

        self.datasetGenerator.playRandomGame()

        self.assertTrue(self.datasetGenerator.game.isOver())

    def test_can_return_boards_history(self):

        self.datasetGenerator.playRandomGame()

        boards = self.datasetGenerator.getBoardHistory()

        game = FourInLine(self.width, self.height)

        expectedBoards = []

        for column in self.blueWinMoves:

            expectedBoards.append(game.getBoard())
            game.insertAt(column)

        expectedBoards.append(game.getBoard())

        for idx in range(len(expectedBoards)):

            self.assertTrue(np.array_equal(boards[idx], expectedBoards[idx]))

    def test_can_return_moves(self):

        self.datasetGenerator.playRandomGame()

        self.assertEqual(self.datasetGenerator.getMoves(), self.blueWinMoves)

    def play_random_game(self, moves: list[int])-> DatasetGenerator:

        datasetGenerator = DatasetGenerator(self.width, self.height, iter(moves))
        datasetGenerator.playRandomGame()

        return datasetGenerator

    def get_real_and_expected_for_winner(self, datasetGenerator: DatasetGenerator, 
                                         realFunc, completeFunc, start: int)-> tuple[list, list]:

        real = realFunc(datasetGenerator)

        complete = completeFunc(datasetGenerator)

        expected = [complete[idx] for idx in range(start, len(complete), 2)]

        return real, expected

    def assert_array_equal_elements_on_lists(self, first: list, second: list):

        for idx in range(len(second)):

            self.assertTrue(np.array_equal(first[idx], second[idx]))

    def assert_can_return_winner_property(self, moves: list[int], realFunc, completeFunc, start: int):

        datasetGenerator = self.play_random_game(moves)

        real, expected = self.get_real_and_expected_for_winner(datasetGenerator,
                                                               realFunc, 
                                                               completeFunc, 
                                                               start)

        self.assert_array_equal_elements_on_lists(real, expected)

    def assert_can_return_winner_input_boards(self, moves: list[int], historyStart: int):

        self.assert_can_return_winner_property(moves, 
                                               DatasetGenerator.getWinnerBoardHistory,
                                               DatasetGenerator.getBoardHistory,
                                               historyStart)

    def test_can_return_winner_input_boards_for_blue(self):

        self.assert_can_return_winner_input_boards(self.blueWinMoves, 0)

    def test_can_return_winner_input_boards_for_red(self):

        self.assert_can_return_winner_input_boards(self.redWinMoves, 1)

    def assert_can_return_winner_moves(self, moves: list[int], movesStart: int):

        self.assert_can_return_winner_property(moves, 
                                               DatasetGenerator.getWinnerMoves,
                                               DatasetGenerator.getMoves,
                                               movesStart)

    def test_can_return_winner_moves_for_blue(self):

        self.assert_can_return_winner_moves(self.blueWinMoves, 0)

    def test_can_return_winner_moves_for_red(self):

        self.assert_can_return_winner_moves(self.redWinMoves, 1)

    def test_raise_exception_when_get_winner_board_history_without_winner(self):

        datasetGenerator = DatasetGenerator(self.width, self.height, iter([]))

        with self.assertRaises(CannotGetWinnerPropertyWhenThereIsNoWinner) as e:

            datasetGenerator.getWinnerBoardHistory()

        self.assertEqual(e.exception.args[0], "Can not get winner property when there is no winner")