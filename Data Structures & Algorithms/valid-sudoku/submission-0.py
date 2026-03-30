class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            elements = set()
            for element in row:
                element = element[0]
                if element in elements:
                    print('a')
                    return False
                if (element < '1' or element > '9') and element != '.':
                    print('b')
                    print(element)
                    return False
                elif element != '.':
                    elements.add(element)
        
        for col in range(len(board[0])):
            elements = set()
            for row in board:
                element = row[col][0]
                if element in elements:
                    print('c')
                    return False
                if (element < '1' or element > '9') and element != '.':
                    print('d')
                    return False
                elif element != '.':
                    elements.add(element)
        
        for row in range(0, len(board), 3):
            for col in range(0, len(board[0]), 3):
                elements = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        element = board[i][j][0]
                        if element in elements:
                            print('e')
                            return False
                        if (element < '1' or element > '9') and element != '.':
                            print('f')
                            return False
                        elif element != '.':
                            elements.add(element)

        return True




        
        