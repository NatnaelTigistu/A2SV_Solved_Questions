class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        '''
        last = 23
        [19,7,2,24,11,16,1,11,23]

        '''
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