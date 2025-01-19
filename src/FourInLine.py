import numpy as np

EMPTY_PLACE = 'O'
BLUE_CHIP = "B"
RED_CHIP = "R"

class CannotInsertUnkownChip(Exception):

    def __init__(self, chip: str):

        super().__init__(f"Cannot insert a chip with value different from BLUE_CHIP or RED_CHIP: given chip value {chip}")

class OutOfRangeColumn(Exception):

    def __init__(self, width: int, column: int):

        super().__init__(f"Column number must be between 0 and {width-1}, but given number was {column}")

class CannotInsertChipOnAFullColumn(Exception):

    def __init__(self, column: int):

        super().__init__(f"Can not insert chip at column {column} because is full")

class CannotGetWinnerWhenThereIsNoWinner(Exception):

    def __init__(self):

        super().__init__("Can not FourInLine.getWinner() when there is no winner. Check before using FourInLine.isThereAWinner()")

class FourInLine:

    def __init__(self, width: int, height: int):

        self.width = width
        self.height = height

        self.board = np.repeat(EMPTY_PLACE, self.width*self.height).reshape((self.height, self.width))

        self.nextChip = BLUE_CHIP

        self.thereIsAWinner = False

    def getBoard(self)-> np.ndarray:

        return self.board
    
    def assertValidChip(self, chip: str):

        if chip != BLUE_CHIP and chip != RED_CHIP:

            raise CannotInsertUnkownChip(chip)

    def assertColumnInRange(self, column: int):

        if not (0 <= column and column < self.width):

            raise OutOfRangeColumn(self.width, column)

    def assertColumnIsNotFull(self, column: int):

        if self.isColumnFull(column):

            raise CannotInsertChipOnAFullColumn(column)

    def insertChipAt(self, chip: str, column: int):

        self.assertValidChip(chip)
        self.assertColumnInRange(column)
        self.assertColumnIsNotFull(column)

        for row in range(self.height):

            if self.board[row][column] == EMPTY_PLACE:

                self.board[row][column] = chip
                break

    def insertAt(self, column: int):

        self.insertChipAt(self.nextChip, column)

        lastChip = self.nextChip

        if lastChip == BLUE_CHIP: self.nextChip = RED_CHIP
        if lastChip == RED_CHIP: self.nextChip = BLUE_CHIP

        self.updateWinner()

    def isColumnFull(self, column: int)-> bool:

        self.assertColumnInRange(column)

        return self.board[self.height-1][column] != EMPTY_PLACE

    def updateConsecutiveChip(self, sameInLine: int, row: int, column: int)-> int:

        if (self.board[row][column] == BLUE_CHIP or
            self.board[row][column] == RED_CHIP):

            sameInLine += 1

            if sameInLine == 3: 
                        
                self.thereIsAWinner = True
                self.winner = self.board[row][column]

        return sameInLine

    def updateWinnerByHorizontal(self):

        sameInLine = 0

        for row in range(self.height):

            for column in range(1, self.width):

                if self.board[row][column-1] == self.board[row][column]:

                    sameInLine = self.updateConsecutiveChip(sameInLine, row, column)

                else: sameInLine = 0

    def updateWinnerByVertical(self):

        sameInLine = 0

        for column in range(self.width):

            for row in range(1, self.height):

                if self.board[row-1][column] == self.board[row][column]:

                    sameInLine = self.updateConsecutiveChip(sameInLine, row, column)

                else: sameInLine = 0

    def updateWinnerByPositiveDiagonal(self):

        for row in range(0, self.height-3):

            for column in range(0, self.width-3):

                if (self.board[row][column] == self.board[row+1][column+1] and
                self.board[row][column] == self.board[row+2][column+2] and
                self.board[row][column] == self.board[row+3][column+3] and
                self.board[row][column] != EMPTY_PLACE):

                    self.thereIsAWinner = True
                    self.winner = self.board[row][column]

    def updateWinnerByNegativeDiagonal(self):

        for row in range(0, self.height-3):

            for column in range(0, self.width-3):

                if (self.board[row+3][column] == self.board[row+2][column+1] and
                self.board[row+3][column] == self.board[row+1][column+2] and
                self.board[row+3][column] == self.board[row][column+3] and
                self.board[row+3][column] != EMPTY_PLACE):

                    self.thereIsAWinner = True
                    self.winner = self.board[row+3][column]

    def updateWinner(self):

        self.updateWinnerByHorizontal()
        self.updateWinnerByVertical()
        self.updateWinnerByPositiveDiagonal()
        self.updateWinnerByNegativeDiagonal()

    def isThereAWinner(self):

        return self.thereIsAWinner
    
    def assertThereIsAWinner(self):

        if not self.isThereAWinner(): raise CannotGetWinnerWhenThereIsNoWinner()

    def getWinner(self)-> str:

        self.assertThereIsAWinner()
        return self.winner

    def isBoardFull(self)-> bool:

        return all([self.isColumnFull(column) for column in range(self.width)])

    def isATie(self):

        return (not self.isThereAWinner()) and self.isBoardFull()
    
    def isOver(self):

        return self.isThereAWinner() or self.isATie()