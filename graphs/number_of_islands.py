# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         if not grid:
#             return 0

#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         islands = 0

#         def bfs(r, c):
#             queue = []
#             visit.add((r, c))
#             queue.append((r, c))

#             while queue:
#                 row, col = queue.pop(0)
#                 directions = [[1,0], [-1, 0], [0, 1], [ 0,-1]]
#                 for dr, dc in directions:
#                     r, c = row + dr, col + dc
#                     if (r in range(rows) and 
#                         c in range(cols) and
#                         grid[r][c] == "1" and
#                         (r, c) not in visit):
#                         queue.append((r, c))
#                         visit.add((r, c))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visit:
#                     bfs(r, c)
#                     islands += 1
#         return islands


#################
#
# DFS SOLUITON FASTER 
#
#################

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        def dfs(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

