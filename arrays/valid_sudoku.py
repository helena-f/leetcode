# Valid Sudoku
# Solved 
# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board = list of lists
        for i, row in enumerate(board):
            # print(i, " ", row)
            # row = list of chars
            rowhash = {}
            # col = char
            for j, col in enumerate(row):
                # print()

                if col != "." and col in rowhash:
                    print("found row duplicate")
                    return False
                else:
                    rowhash[col] = 1

                # col search
                if i == 0:
                    colhash = {}
                    for row_index in range(9):
                        curr_val = board[row_index][j]
                        # print(curr_val)
                        if curr_val != "." and curr_val in colhash:
                            print("found col duplicate")
                            return False
                        else:
                            colhash[curr_val] = 1

        sqhash = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in sqhash[(i // 3, j // 3)]:
                    return False
                
                sqhash[(i // 3, j // 3)].add(board[i][j])
        
        return True