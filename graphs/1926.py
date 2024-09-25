class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        # bfs 
        # out of bound without hitting a + W
        # else if hits plus and doesnt go out no exit

        ROWS, COLS = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])  # (x, y, steps)
        visited = set([(entrance[0], entrance[1])])

        while q:
            x, y, steps = q.popleft()

            # Check if we've reached an exit
            if (x == 0 or y == 0 or x == ROWS - 1 or y == COLS - 1) and [x, y] != entrance:
                return steps

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_x, new_y = x + dx, y + dy

                if (0 <= new_x < ROWS and 0 <= new_y < COLS and
                    maze[new_x][new_y] == "." and (new_x, new_y) not in visited):
                    q.append((new_x, new_y, steps + 1))
                    visited.add((new_x, new_y))

        return -1  # No exit found