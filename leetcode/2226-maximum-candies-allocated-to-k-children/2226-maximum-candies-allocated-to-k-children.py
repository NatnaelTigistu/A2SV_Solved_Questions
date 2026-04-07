class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        
        def can_distribute(mid):
            count = 0
            for candy in candies:
                count += candy // mid
                if count >= k:
                    return True
            return False
        
        total = sum(candies)
        if total < k:
            return 0  
        low, high, result = 1, total // k, 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_distribute(mid):
                result = mid  
                low = mid + 1  
            else:
                high = mid - 1  
        
        return result