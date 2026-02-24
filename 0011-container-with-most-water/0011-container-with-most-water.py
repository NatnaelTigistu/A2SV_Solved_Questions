class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1
        best = 0
        
        while left < right:
            width = right - left
            _height = min(height[left] , height[right])
            best = max(best, width*_height)
            if height[right]>height[left]:
                left += 1
            else:
                right -= 1
        return best