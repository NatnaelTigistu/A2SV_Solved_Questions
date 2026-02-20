class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) # number of piles
        piles = sorted(piles,reverse = True) 
        maximumCoins = 0 # maximum number of coins

        # in descending sorted set of piles the maximum u can get is the sum of the n//3 piles starting from second and jumping one pile 
        i = 1 # to track the piles
        for _ in range(n // 3):
            maximumCoins += piles[i]
            i += 2
        return maximumCoins