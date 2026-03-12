class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums) # number of elements in nums
        nums = sorted(nums)
        print(nums)

        for i in range(n-1,-1,-1):
            x , y , z = nums[i] , nums[i-1] , nums[i-2]
            if i > 1 and x < y + z:
                return x+y+z
        return 0