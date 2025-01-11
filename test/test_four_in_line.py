import unittest
from src.FourInLine import *

class TestFourInLine(unittest.TestCase):

    def setUp(self):

        self.width = 5
        self.height = 7

        self.game = FourInLine(self.width, self.height)

    def test_initialize_with_empty_board(self):

        board = self.game.getBoard()

        self.assertEqual(board.shape[0], self.height)
        self.assertEqual(board.shape[1], self.width)

        for row in range(self.height):

            for column in range(self.width):

                self.assertEqual(board[row][column], 'O')

    def test_can_insert_chip_on_column(self):

        self.game.insertChipAt(BLUE_CHIP, 0)

        board = self.game.getBoard()

        self.assertEqual(board[0][0], BLUE_CHIP)

    def test_can_insert_chip_over_another_chip(self):

        self.game.insertChipAt(BLUE_CHIP, 3)
        self.game.insertChipAt(BLUE_CHIP, 3)

        board = self.game.getBoard()

        self.assertEqual(board[1][3], BLUE_CHIP)
        self.assertEqual(board[2][3], EMPTY_PLACE)

    def test_can_check_if_a_column_is_full(self):

        for row in range(self.height-1):

            self.game.insertChipAt(BLUE_CHIP, 2)

        self.assertFalse(self.game.isColumnFull(2))

        self.game.insertChipAt(BLUE_CHIP, 2)

        self.assertTrue(self.game.isColumnFull(2))

    def test_can_take_turns(self):

        self.game.insertAt(0)
        self.game.insertAt(1)
        self.game.insertAt(1)
        self.game.insertAt(0)

        board = self.game.getBoard()

        self.assertEqual(board[0][0], BLUE_CHIP)
        self.assertEqual(board[0][1], RED_CHIP)
        self.assertEqual(board[1][1], BLUE_CHIP)
        self.assertEqual(board[1][0], RED_CHIP)

    def play_until_almost_win_by_horizontal(self):

        for column in range(3):

            self.game.insertAt(column)
            self.game.insertAt(column)

    def test_can_check_when_winner_by_horizontal_line_on_first_row(self):

        self.play_until_almost_win_by_horizontal()

        self.assertFalse(self.game.isThereAWinner())

        self.game.insertAt(3)

        self.assertTrue(self.game.isThereAWinner())

    def test_can_check_when_winner_by_horizontal_line(self):

        self.play_until_almost_win_by_horizontal()

        self.game.insertAt(0)
        self.game.insertAt(3)
        self.game.insertAt(1)

        self.assertFalse(self.game.isThereAWinner())

        self.game.insertAt(3)

        self.assertTrue(self.game.isThereAWinner())

    def test_can_check_who_is_the_winner_by_horizontal(self):

        self.play_until_almost_win_by_horizontal()

        self.game.insertAt(3)

        self.assertEqual(self.game.getWinner(), BLUE_CHIP)

    def play_until_almost_win_by_vertical(self):

        for row in range(3):

            self.game.insertAt(0)
            self.game.insertAt(1)

    def test_can_check_when_and_who_is_the_winner_by_vertical_line(self):

        self.play_until_almost_win_by_vertical()

        self.game.insertAt(2)

        self.assertFalse(self.game.isThereAWinner())

        self.game.insertAt(1)

        self.assertTrue(self.game.isThereAWinner())

        self.assertEqual(self.game.getWinner(), RED_CHIP)

    def test_can_check_when_winner_by_positive_diagonal_line(self):

        self.assertTrue(False)

    def test_can_check_when_winner_by_negative_diagonal_line(self):

        self.assertTrue(False)

    def test_can_check_if_there_is_a_winner(self):

        self.assertTrue(False)

    def test_can_check_who_is_the_winner(self):

        self.assertTrue(False)

    def test_can_check_if_there_is_a_tie(self):

        self.assertTrue(False)

    def test_can_check_if_game_is_over(self):

        self.assertTrue(False)

    def test_raise_error_when_trying_to_insert_unknow_chip(self):

        self.game.insertChipAt(BLUE_CHIP, 0)
        self.game.insertChipAt(RED_CHIP, 1)

        unkownChip = "unkown chip"

        with self.assertRaises(CannotInsertUnkownChip) as e:

            self.game.insertChipAt(unkownChip, 2)

        self.assertEqual(e.exception.args[0], f"Cannot insert a chip with value different from BLUE_CHIP or RED_CHIP: given chip value {unkownChip}")

    def get_out_of_range_message(self, column: int)-> str:

        return f"Column number must be between 0 and {self.width-1}, but given number was {column}"

    def test_raise_error_when_trying_to_insert_chip_at_out_of_range_column(self):

        with self.assertRaises(OutOfRangeColumn) as e:

            self.game.insertChipAt(BLUE_CHIP, -1)

        self.assertEqual(e.exception.args[0], self.get_out_of_range_message(-1))

        with self.assertRaises(OutOfRangeColumn) as e:

            self.game.insertChipAt(BLUE_CHIP, self.width)

        self.assertEqual(e.exception.args[0], self.get_out_of_range_message(self.width))

    def test_raise_error_when_insert_chip_on_a_full_column(self):

        column = 2

        for row in range(self.height):

            self.game.insertChipAt(BLUE_CHIP, column)

        self.assertTrue(self.game.isColumnFull(column))

        with self.assertRaises(CannotInsertChipOnAFullColumn) as e:

            self.game.insertChipAt(BLUE_CHIP, column)

        self.assertEqual(e.exception.args[0], f"Can not insert chip at column {column} because is full")

    def test_raise_error_when_checking_full_column_at_out_of_range_column(self):

        with self.assertRaises(OutOfRangeColumn) as e:

            self.game.isColumnFull(-1)

        self.assertEqual(e.exception.args[0], self.get_out_of_range_message(-1))

        with self.assertRaises(OutOfRangeColumn) as e:

            self.game.isColumnFull(self.width)

        self.assertEqual(e.exception.args[0], self.get_out_of_range_message(self.width))

    def test_raise_error_when_checking_winner_with_no_winner(self):

        self.assertTrue(False)

    def test_raise_error_when_inserting_chip_at_game_over(self):

        self.assertTrue(False)