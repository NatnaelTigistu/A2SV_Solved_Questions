class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        
        if nums[0] != 0:
            return 0
        if nums[j] != j+1:
            return j+1
  
        while j > i:
            if nums[i+1] != nums[i] + 1:
                return nums[i] + 1
            if nums[j-1] != nums[j] - 1:
                return nums[j] - 1
            i,j = i+1,j-1
