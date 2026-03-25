class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ops = 0
        postfix = 0 
        current = 1
        
        for i in range(len(nums)):
            if postfix >= n:
                return ops

            while nums[i] > postfix+1 and nums[i] != 1: 
                if postfix >= n:
                    return ops
                postfix += current 
                current = postfix + 1 
                ops += 1 
            postfix += nums[i] 
            current = postfix + 1 

        while postfix < n:
            postfix += current
            current = postfix + 1
            ops += 1
            
        return ops
