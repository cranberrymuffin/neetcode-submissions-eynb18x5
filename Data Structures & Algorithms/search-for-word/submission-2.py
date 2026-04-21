class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for rowIdx, _ in enumerate(board):
            for colIdx, _ in enumerate(board[rowIdx]):
                if self.visitWord(rowIdx, colIdx, board, word, []):
                    return True
        return False
    def visitWord(self, startRow: int, startCol: int, board: List[List[str]], word: str, visited: List[tuple[int, int]]) -> bool:
        rowCol = (startRow, startCol)
        if len(word) == 0:
            return True
        if startRow < 0 or startRow >= len(board) or startCol < 0 or startCol >= len(board[startRow]) or board[startRow][startCol] != word[0] or rowCol in visited:
            return False
        else:
            return self.visitWord(startRow + 1, startCol, board, word[1:], visited + [rowCol]) or self.visitWord(startRow - 1, startCol, board, word[1:], visited + [rowCol]) or self.visitWord(startRow, startCol - 1, board, word[1:], visited + [rowCol]) or self.visitWord(startRow, startCol + 1, board, word[1:], visited + [rowCol])


        
        