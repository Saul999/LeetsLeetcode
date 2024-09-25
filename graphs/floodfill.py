class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        
        ROWS, COLS = len(image), len(image[0])
        q = deque([(sr, sc)])
        visited = set([(sr, sc)])
        startingPixel = image[sr][sc]
        while q:
            x, y = q.popleft()
            image[x][y] = color
            for dx, dy in ((1,0), (-1,0), (0,-1), (0,1)):
                xVal = x + dx
                yVal = y + dy
                if 0 <= yVal < COLS and 0 <= xVal < ROWS and image[xVal][yVal] == startingPixel and (xVal, yVal) not in visited:
                    q.append([xVal, yVal])
                    visited.add((xVal, yVal))
        return image