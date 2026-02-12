class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)
        # check the existence of each charachter in ransomeNote in magazine and remove if it exist
        for char in ransomNote:
            if char not in magazine:
                return False
            magazine[char] -= 1
            if magazine[char] == 0:
                del magazine[char]
        return True