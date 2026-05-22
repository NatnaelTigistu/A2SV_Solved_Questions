class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def backtrack(rm,rn):
            nonlocal m , n
            if rn == n or rm == m:
                return 1 
            if (rm,rn) in dp:
                return dp[(rm,rn)]
            res = (backtrack(rm + 1,rn) + backtrack(rm , rn + 1))
            dp[(rm,rn)] = res
            return res
        return backtrack(1,1)