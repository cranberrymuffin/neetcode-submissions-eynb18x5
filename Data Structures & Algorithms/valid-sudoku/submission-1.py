class Solution:
    def isValidRows(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            items = set()
            for item in board[r]:
                if item in items:
                    print("invalid rows")
                    return False
                if item != '.':
                    items.add(item)
        return True

    def isValidCols(self, board: List[List[str]]) -> bool:
        for c in range(len(board[0])):
            items = set()
            for r in range(len(board[c])):
                item = board[r][c]
                if item in items:
                    print("invalid cols")
                    return False
                if item != '.':
                    items.add(item)
        return True

    def isValid3x3s(self, board: List[List[str]]) -> bool:
        for rowStart in range(0,9,3):
            for colStart in range(0,9,3):
                items = set()
                for r in range(rowStart, rowStart+3):
                    for c in range(colStart, colStart+3):
                        item = board[r][c]
                        if item in items:
                            print(item)
                            return False
                        if item != '.':
                            items.add(item)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRows(board) and self.isValidCols(board) and self.isValid3x3s(board)

        