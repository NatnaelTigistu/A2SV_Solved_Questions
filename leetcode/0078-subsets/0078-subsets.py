class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res =[]
        def backtrack (s,e):
            if s>len(nums):
                return 
            res.append(e.copy())
            for i in range(s,len(nums)):
                e.append(nums[i])
                backtrack (i+1,e)
                e.pop()
        backtrack (0,[])
        return res