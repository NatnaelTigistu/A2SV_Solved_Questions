class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [f for f in range(1,n+1)]
        i = 0
        k -= 1
        while len(friends) > 1:
            i = (i+k) % len(friends)
            del friends[i]

        return friends[0]