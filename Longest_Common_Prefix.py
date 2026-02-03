class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        firstWord = strs[0]
        for i in range(len(firstWord)):
            char = firstWord[i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return firstWord[:i]
        return firstWord
