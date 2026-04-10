class Solution:
    def isValidRow(self, board: List[List[str]], r: int):
        seen = set()
        for c in range(9):
            num = board[r][c]
            if num in seen:
                return False
            if ord(num) >= ord('1') and ord(num) <= ord('9'):
                seen.add(num)
        return True

    def isValidCol(self, board: List[List[str]], c: int):
        seen = set()
        for r in range(9):
            num = board[r][c]
            if num in seen:
                return False
            if ord(num) >= ord('1') and ord(num) <= ord('9'):
                seen.add(num)
        return True

    def isValid3x3(self, board: List[List[str]], row: int, col: int):
        seen = set()
        for r in range(row, row + 3, 1):
            for c in range(col, col+3, 1):
                num = board[r][c]
                if num in seen:
                    return False
                if ord(num) >= ord('1') and ord(num) <= ord('9'):
                    seen.add(num)
        return True



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidRow(board, i):
                print('invalid row')
                return False
            if not self.isValidCol(board, i):
                print('invalid col')
                return False
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not self.isValid3x3(board, r, c):
                    print('invalid 3x3')
                    return False
        return True
        
        
        