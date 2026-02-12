class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        result = []
        for x, count in freq.items():
            if count > n // 3:
                result.append(x)

        return result