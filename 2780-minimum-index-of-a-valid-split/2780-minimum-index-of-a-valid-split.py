class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        # boyer - moore majority vote algorithm
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
 
        total = nums.count(candidate)
        
        left_count = 0
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] == candidate:
                left_count += 1
            
            left_length = i + 1
            right_length = n - left_length
            right_count = total - left_count
            
            if (left_count * 2 > left_length and
                right_count * 2 > right_length):
                return i
        
        return -1