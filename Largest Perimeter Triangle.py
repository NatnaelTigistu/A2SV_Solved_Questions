class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums) # number of elements in nums
        found = False
        nums = sorted(nums,reverse = True)

        for i in range(n - 2):
            x , y , z = nums[i] , nums[i+1] , nums[i+2]
            if x < y + z:
                return x+y+z
        return 0