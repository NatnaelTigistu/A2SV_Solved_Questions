import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = k - 1
        left, right = 0, len(nums) - 1

        while True:
            pivot = nums[random.randint(left, right)]
            i, j = left, right

            while i <= j:
                while nums[i] > pivot:
                    i += 1
                while nums[j] < pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            if k <= j:
                right = j
            elif k >= i:
                left = i
            else:
                return nums[k]