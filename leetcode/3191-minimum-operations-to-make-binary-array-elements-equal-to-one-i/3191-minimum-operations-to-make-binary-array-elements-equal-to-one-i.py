class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        oprations = 0

        for i in range(n):
            if nums[i] == 0:
                if i+2 >= n:
                    return -1
                nums[i+1] = 1-nums[i+1]
                nums[i+2] = 1-nums[i+2]
                oprations += 1
        return oprations