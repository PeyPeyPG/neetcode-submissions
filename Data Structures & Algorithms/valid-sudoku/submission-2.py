class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        group = 0

        for i in range(9):
            for j in range(9):
                if i < 3:
                    if j < 3:
                        group = 0
                    elif j < 6:
                        group = 1
                    else:
                        group = 2
                elif i < 6:
                    if j < 3:
                        group = 3
                    elif j < 6:
                        group = 4
                    else:
                        group = 5
                else:
                    if j < 3:
                        group = 6
                    elif j < 6:
                        group = 7
                    else:
                        group = 8

                if board[i][j] != '.':
                    if board[i][j] in rows[i]:
                        return False
                    if board[i][j] in cols[j]:
                        return False
                    if board[i][j] in boxes[group]:
                        return False
                
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[group].add(board[i][j])
        
        return True
                

