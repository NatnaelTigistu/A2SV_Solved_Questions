class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif not haystack:
            return -1
        else:
            h = len(haystack)
            n = len(needle)
            for i in range(h-n+1):
                if haystack[i:i+n] == needle:
                    return i
            return -1