class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # start at 0,0
        num_islands = 0
        # keep a visited array
        visited = set()

        def is_valid_path(row,col):
            # return if in bounds, not in visited, is 1
            # if no more valid paths to take from invalid indices, 
            # or surrounded by already visited nodes
            if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) 
                    or (row, col) in visited or grid[row][col] != "1"):
                    return False
            else:
                return True

        def get_island(row, col):    
            visited.add((row,col))
            # up, down, right, left
            directions = [(1,0), (-1, 0), (0,1), (0,-1)]
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if is_valid_path(new_row, new_col):
                    # if hit 1, use DFS to follow the linked path of 1s
                    # found a valid path, use dfs to continue traversing
                    # add to visited list
                    get_island(new_row, new_col)
        # traverse array with nested for loops if hitting 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if is_valid_path(row, col):
                    # we have found 1 complete island and add it to counter
                    num_islands += 1
                    get_island(row, col)
                # else is 0 or already visited and we want to skip over


        # return counter of islands visited
        return num_islands

