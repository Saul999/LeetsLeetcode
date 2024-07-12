class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def bfs(grid,i ,j):
            q = deque([(i, j)])
            while q:
                grid[i][j] = "0"
                x, y = q.popleft()
                for dx, dy in [(1,0),(-1,0), (0,1), (0,-1)]:
                    tempx = dx + x
                    tempy = dy + y
                    if 0 <= tempx < len(grid) and 0 <= tempy < len(grid[0]) and grid[tempx][tempy] == '1':
                        q.append((tempx, tempy))
                        grid[tempx][tempy] = '0'
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    bfs(grid, i , j)
                    islands += 1
        
        return islands