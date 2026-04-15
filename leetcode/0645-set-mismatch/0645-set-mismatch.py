class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        res = [0,0]
        counter = [0] *(n)
        for i in nums:
            counter[i] += 1
        for i in range(1,n):
            if counter[i] == 0:
                res[1] = i
            elif counter[i] == 2:
                res[0] = i
            
        return res
                