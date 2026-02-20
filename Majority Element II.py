class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        reqFreq = n // 3
        base = min(nums)
        arrSize = (max(nums) - base) + 1
        arr = [0]* arrSize

        for num in nums:
            arr[num - base] += 1
        res = []
        for i in range(arrSize):
            if arr[i] > reqFreq:
                res.append(i + base)
        
        return res