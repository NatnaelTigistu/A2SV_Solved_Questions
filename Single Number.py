class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i in seen:
                del seen[i]
            else:
                seen[i] = i
        for i in seen:
            return seen[i]