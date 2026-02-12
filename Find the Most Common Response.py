class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        if not responses:
            return ""
        freq = {}
        highestFreq = 0
        commonWords = []
        for response in responses:
            response = set(response)
            for term in response:
                freq[term] = freq.get(term,0) + 1
                highestFreq = max(highestFreq,freq[term])
        for terms in freq:
            if freq[terms] == highestFreq:
                commonWords.append(terms)
        sortedWords = sorted(sorted(commonWords,key = len))
        return sortedWords[0]