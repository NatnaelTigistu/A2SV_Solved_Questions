class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = {}
        res = []
        for i in nums:
            if i in visited:
                res.append(i)
            else:
                visited[i] = True
        return res