class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        res = ''.join(char * count for char,count in sorted(freq.items(),key = lambda x : (-x[1],x[0])))
        return res