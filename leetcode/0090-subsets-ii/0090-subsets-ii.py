class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        visited = set()
        def backtrack (s,e):
            if s>len(nums):
                return 
            key = tuple(sorted(e.copy()))
            if tuple(key) not in visited:
                res.append(e.copy())
            visited.add(key)
            for i in range(s,len(nums)):
                e.append(nums[i])
                backtrack (i+1,e)
                e.pop()
        backtrack (0,[])
        return res