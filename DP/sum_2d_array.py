class NumMatrix:
    # 6 3
    # 2 0

    # 6 9
    # 8 11

    # 11 = right + above - corner + currval
    def __init__(self, matrix: List[List[int]]):
        # build cumulative sum over each value of the matrix
        # O(n^2)
        nrows = len(matrix)
        ncols = len(matrix[0])
        self.sum = [[0] * (ncols + 1) for _ in range(nrows + 1)]
        for row in range(1, nrows + 1):
            for col in range(1, ncols + 1):
                self.sum[row][col] = (self.sum[row][col - 1] 
                    + self.sum[row - 1][col] 
                    - self.sum[row - 1][col - 1] 
                    + matrix[row - 1][col - 1])

    # 3 2 1
    # 0 1 5

    # x 0 1 2
    # 0 3 5 6 
    # 1 3 6 12

    # 12 = 6 + 6 - 5 + 5

    # find sum (1,1) to (1,2) = 6
    # (row1, col1) to (row2, col2)
    # total - sum[1,0] - sum[0,2] + overlap sum[0,0] = 3 + 6 - 3 = 6
    # sum [row2][col2] - sum[row2, col1 - 1] - sum[row1 - 1, col2] + sum[row1 - 1, col1 - 1]
    
    # given sum from 0,0 to i,j, find the subtracted area 
    # get the left and right area above the rectangle and subtract it
    # but you subtract it twice so add it back

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.sum[row2 + 1][col2 + 1]
                - self.sum[row2 + 1][col1] 
                - self.sum[row1][col2 + 1] 
                + self.sum[row1][col1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)