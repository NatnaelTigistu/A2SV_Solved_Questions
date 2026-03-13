class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True
        nums = reversed(nums)
        nums = list(nums)[1:]
        r_j = 1
        for num in nums:
            if num >= r_j:
                r_j = 1
            else:
                r_j += 1
        if r_j == 1:
            return True
        return False
