class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            verificationSet = set()
            for column in range(9):
                num = board[row][column]
                if num in verificationSet: 
                    return False
                elif num != ".":
                    verificationSet.add(num)
        for column in range(9):
            verificationSet = set()
            for row in range(9):
                num = board[row][column]
                if num in verificationSet: 
                    return False
                elif num != ".":
                    verificationSet.add(num)
        for square in range(9):
            verificationSet = set()
            for row in range(3):
                for column in range(3):
                    num = board[3*(square//3) + row][3*(square%3) + column]
                    if num in verificationSet: 
                        return False
                    elif num != ".":
                        verificationSet.add(num)
        return True
