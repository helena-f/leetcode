class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0, len(matrix) - 1
        while l_row <= r_row:
            mid = l_row + ((r_row - l_row) // 2)
            # if the first element is less than or equal to
            # and the last element is greater than or equal to
            # we're in the right row
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]:
                l_row = mid 
                break
            # if mid less, move right -> mid 
            elif target < matrix[mid][0]:
                r_row = mid - 1
            # if mid more, move left -> mid
            else:
                l_row = mid + 1

        if 0 > l_row or l_row > len(matrix) - 1:
            return False

        l_col, r_col = 0, len(matrix[0]) - 1
        while l_col <= r_col:
            mid = l_col + ((r_col - l_col) // 2)
            if matrix[l_row][mid] == target:
                return True
            elif matrix[l_row][mid] < target:
                l_col = mid + 1
            else: 
                r_col = mid - 1

        return False