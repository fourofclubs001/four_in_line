import numpy as np

EMPTY_PLACE = 'O'
BLUE_CHIP = "B"
RED_CHIP = "R"

class CannotInsertUnkownChip(Exception):

    def __init__(self, chip: str):

        super().__init__(f"Cannot insert a chip with value different from BLUE_CHIP or RED_CHIP: given chip value {chip}")

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

        self.board[0][column] = chip 