class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)   
        res = []
        ans = []

        def backtrack(start):
            nonlocal ans, res

            if start == len(s):
                ans.append(" ".join(res))
                return

            word = ""
            for i in range(start, len(s)):
                word += s[i]
                if word in wordDict:
                    res.append(word)
                    backtrack(i + 1)
                    res.pop()

        backtrack(0)
        return ans