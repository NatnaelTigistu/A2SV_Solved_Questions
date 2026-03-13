class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers = Counter(answers)
        total = 0
        for r in answers:
            gr_size = r + 1
            gr = ceil(answers[r] / gr_size)
            total += gr * gr_size
        return total