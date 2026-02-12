class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1) 
        nums2 = set(nums2)
        res = []
        # append elements if they exits on both sets
        for i in nums1:
            if i in nums2:
                res.append(i)
        return res