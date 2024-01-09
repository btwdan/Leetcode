from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        	return -1
        
        q = deque([(0, 0, 1)])
        visited = set([(0, 0)])
    
        while q:
            i, j, length = q.popleft()
            if i == j == n-1:
                return length
        
            for ni, nj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1), (i+1,j+1), (i+1,j-1), (i-1,j+1), (i-1,j-1)):
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0 and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    q.append((ni, nj, length+1))
                
        return -1