class NumArray:

    def __init__(self, nums: List[int]):
        
        self.pref_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.pref_sum[i+1] = self.pref_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        
        return  self.pref_sum[right+1] - self.pref_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)