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

    def test_raise_error_when_trying_to_insert_unknow_chip(self):

        self.game.insertChipAt(BLUE_CHIP, 0)
        self.game.insertChipAt(RED_CHIP, 1)

        unkownChip = "unkown chip"

        with self.assertRaises(CannotInsertUnkownChip) as e:

            self.game.insertChipAt(unkownChip, 2)

        self.assertEqual(e.exception.args[0], f"Cannot insert a chip with value different from BLUE_CHIP or RED_CHIP: given chip value {unkownChip}")

    def test_raise_error_when_trying_to_insert_chip_in_out_of_range_column(self):

        with self.assertRaises(CannotInsertChipAtOutOfRangeColumn) as e:

            self.game.insertChipAt(BLUE_CHIP, -1)

        self.assertEqual(e.exception.args[0], f"Can not insert chip at out of range column. Column number must be between 0 and {self.width-1}, but given number was -1")

        with self.assertRaises(CannotInsertChipAtOutOfRangeColumn) as e:

            self.game.insertChipAt(BLUE_CHIP, self.width)

        self.assertEqual(e.exception.args[0], f"Can not insert chip at out of range column. Column number must be between 0 and {self.width-1}, but given number was {self.width}")