class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        m = len(grid)
        n = len(grid[0])

        def backtrack(r, c):
            if r >= m or c >= n:
                return float('inf')
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            if (r, c) in dp:
                return dp[(r, c)]

            dp[(r, c)] = grid[r][c] + min(
                backtrack(r + 1, c),
                backtrack(r, c + 1)
            )
            return dp[(r, c)]

        return backtrack(0, 0)