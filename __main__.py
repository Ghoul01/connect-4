from re import S


class Board():
    
    def __init__(self):
        self.board = [
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."]
            ]
        
        
    """
        Hello, this is my function defininton
    """
    def print(self):

        em = ""
        for y in self.board:
            for x in y:
                em += x + " "
            em += "\n"
        print(em)
    
    def dropD(self, col):
        # self.board[0][0] = "X"
        row = 5
        while self.board[row][col] != ".":
            row -= 1
        
        self.board[row][col] = "X"
        
        


myBoard = Board()
myBoard.dropD(0)
myBoard.print()

myboard2 = Board()
