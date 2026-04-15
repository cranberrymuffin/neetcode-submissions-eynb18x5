class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow = 0
        endRow = len(matrix) - 1
        startCol = 0
        endCol = len(matrix[0]) - 1
        while startRow <= endRow and startCol <= endCol:
            middleRow = (startRow + endRow) // 2
            middleCol = (startCol + endCol) // 2

            if matrix[middleRow][0] > target:
                endRow = middleRow - 1
            elif matrix[middleRow][len(matrix[middleRow]) - 1] < target:
                startRow = middleRow + 1
            else:
                if matrix[middleRow][middleCol] == target:
                    return True
                elif matrix[middleRow][middleCol] < target:
                    startCol = middleCol + 1
                else:
                    endCol = middleCol - 1

        return False

