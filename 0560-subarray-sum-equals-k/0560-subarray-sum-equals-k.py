class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = {}
        pref[0] = 1

        _sum = 0
        count = 0
        for num in nums:
            _sum += num
            count += pref.get(_sum - k , 0)
            pref[_sum] = pref.get(_sum , 0) + 1
        return count