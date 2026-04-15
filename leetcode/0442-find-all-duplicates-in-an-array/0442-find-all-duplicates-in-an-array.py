class Solution:
    #1 2 3 4 3 2 7 8
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        dup = set()
        while i < len(nums):
            if nums[i] == i+1:
                i += 1
                continue
            elif nums[i] == nums[nums[i]-1]:
                dup.add(nums[i])
                i += 1
            else:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        return list(dup)