class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for n,i in enumerate(nums):
            compliment = target - i
            if compliment in compliments:
                return [n,compliments[compliment]]
            compliments[i] = n
        return [-1,-1]