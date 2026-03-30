class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def backtrack(e):
            if len(res) == k:
                return
      
            if len(e) == n:
                #append and return
                res.append(''.join(c for c in e))
                return 

            if e[-1] == 'a':
                e.append('b')
                backtrack(e)
                e.pop()
                e.append('c')
                backtrack(e)
                e.pop()
            elif e[-1] == 'b':
                e.append('a')
                backtrack(e)
                e.pop()
                e.append('c')
                backtrack(e)
                e.pop()
            else:
                e.append('a')
                backtrack(e)
                e.pop()
                e.append('b')
                backtrack(e)
                e.pop()
        for char in ['a','b','c']:
            if len(res) == k:
                break
            backtrack([char])
        print(res)
        if len(res) == k:
            return res[k-1]
        return ""