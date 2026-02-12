class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns
        zeroPos = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroPos.append([i,j])
        for pos in zeroPos:
            i,j = pos[0],pos[1]
            for p in range(n):
                matrix[i][p] = 0
            for v in range(m):
                matrix[v][j] = 0