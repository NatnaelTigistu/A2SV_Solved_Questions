class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        indices = {} 

        for j in range(len(nums)):
            num = nums[j]

            if num in indices:
                for i in indices[num]:
                    if (i * j) % k == 0:
                        count += 1
            else:
                indices[num] = []

            indices[num].append(j)

        return count