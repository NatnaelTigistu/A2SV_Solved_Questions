class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n==0 or k==0:
            return []
        res = []
        def backtrack(s,c):
            if len(c) == k:
                res.append(c.copy())
                return 
            for i in range(s,n+1):
                c.append(i)
                backtrack(i+1,c)
                c.pop()
        backtrack(1,[])
        return res