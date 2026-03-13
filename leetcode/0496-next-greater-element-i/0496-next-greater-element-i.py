class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = defaultdict(lambda : -1)
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            
            greater[num] = stack[-1] if stack else -1
            stack.append(num)
        return [greater[n] for n in nums1]