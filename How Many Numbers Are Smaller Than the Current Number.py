class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums) # number of elements in nums
        smallerNums = {}
        for num in nums:
            smallerNums[num] = 0

        sortedNums = sorted(nums, reverse = True)
        for num in sortedNums:
            smallerNums[num] = n-1
            n -= 1
        res = []
        for num in nums:
            res.append(smallerNums[num])
        return res