class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False
        wordMap = {}
        usedWords = {}
        for char,word in zip(pattern,words):
            if word not in usedWords and char not in wordMap:
                wordMap[char] = word
                usedWords[word] = char
                continue
            if word in usedWords and usedWords[word] != char:
                return False
            if word != wordMap[char]:
                return False

        return True