import numpy as np

EMPTY_PLACE = 'O'
BLUE_CHIP = "B"
RED_CHIP = "R"

class CannotInsertUnkownChip(Exception):

    def __init__(self, chip: str):

        super().__init__(f"Cannot insert a chip with value different from BLUE_CHIP or RED_CHIP: given chip value {chip}")

class CannotInsertChipAtOutOfRangeColumn(Exception):

    def __init__(self, width: int, outOfRangeColumn: int):

        super().__init__(f"Can not insert chip at out of range column. Column number must be between 0 and {width-1}, but given number was {outOfRangeColumn}")

class FourInLine:

    def __init__(self, width: int, height: int):

        self.width = width
        self.height = height

        self.board = np.repeat(EMPTY_PLACE, self.width*self.height).reshape((self.height, self.width))

    def getBoard(self)-> np.ndarray:

        return self.board
    
    def insertChipAt(self, chip: str, column: int):

        if chip != BLUE_CHIP and chip != RED_CHIP:

            raise CannotInsertUnkownChip(chip)
        
        if not (0 <= column and column < self.width):

            raise CannotInsertChipAtOutOfRangeColumn(self.width, column)

        self.board[0][column] = chip 