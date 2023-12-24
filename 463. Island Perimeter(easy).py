class Solution(object):
    def islandPerimeter(self, grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i != 0:
                        if grid[i - 1][j] == 0:
                            res += 1
                    else:
                        res += 1
                    if j != 0:
                        if grid[i][j - 1] == 0:
                            res += 1
                    else:
                        res += 1
                    if i != (len(grid) - 1):
                        if grid[i + 1][j] == 0:
                            res += 1
                    else:
                        res += 1 
                    if j != (len(grid[i]) - 1):
                        if grid[i][j + 1] == 0:
                            res += 1
                    else:
                        res += 1
        return res