class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix) # n is the number of rows
        m = len(matrix[0]) # m is the number of columns

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = matrix[j][i]
        return res