class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            count = max(count , 0)
            if log == "../":
                count -= 1
            elif log == "./":
                continue
            else:
                count += 1
        return max(count, 0)