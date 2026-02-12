class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        sortedList = sorted([[num,freqc] for num,freqc in freq.items()],key = lambda element: element[1],reverse = True)
        for _ in range(k):
            res.append(sortedList[_][0])
        
        return res