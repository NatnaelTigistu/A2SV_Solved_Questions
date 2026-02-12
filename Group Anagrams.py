class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key = ''.join(a for a in sorted(word))
            if key not in group:
                group[key] = []
            group[key].append(word)
        anagrams = []
        for anagram in group.values():
            anagrams.append(anagram)
        return anagrams