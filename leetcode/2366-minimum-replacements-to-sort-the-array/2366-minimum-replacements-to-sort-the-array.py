class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        ops = 0 
        last = nums[-1]
        
        for i in range(len(nums)-2,-1,-1):
            
            if nums[i] > last:
                quotient = ceil(nums[i] / last)
                last = nums[i] // quotient
                ops += quotient - 1
            else:
                last = nums[i]

        return ops