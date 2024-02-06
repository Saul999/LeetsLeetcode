class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = len(matrix[0])  # 4
        cols = len(matrix)  # 3

        finalval = 0
        while finalval != target:
            colCounter = -1
            rowCounter = -1
            if cols[colCounter] > target:
                colCounter -= 1
            elif rows[rowCounter] > target:
                rowCounter -= 1
            elif rows[rowCounter] == target:
                finalval = target
                return rows, cols
