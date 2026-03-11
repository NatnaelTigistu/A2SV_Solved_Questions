class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = deque()
        min_dq = deque()
        max_su = 0
        l = 0
        for r in range(len(nums)):
            while max_dq and nums[r] > max_dq[-1]:
                max_dq.pop()
            while min_dq and nums[r] < min_dq[-1]:
                min_dq.pop()

            max_dq.append(nums[r])
            min_dq.append(nums[r])

            while max_dq[0] - min_dq[0] > limit:
                if max_dq[0] == nums[l]:
                    max_dq.popleft()
                if min_dq[0] == nums[l]:
                    min_dq.popleft()
                l += 1

            max_su = max(max_su , r - l + 1)
        return max_su