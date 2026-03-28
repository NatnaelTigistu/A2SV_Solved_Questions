class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        visited = set()
        def backtrack (s,e):
            if s > len(nums):
                return 
            if len(e) > 1 and e[-2] > e[-1]:
                return

            key = tuple(sorted(e.copy()))
            if tuple(key) not in visited and tuple(e.copy()) == key and len(e) > 1:
                res.append(e.copy())
            visited.add(key)
           
            for i in range(s,len(nums)):
                e.append(nums[i])
                backtrack (i+1,e)
                e.pop()
        backtrack (0,[])
        return res