class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = len(people)
        people.sort()

        heaviest = p-1
        lightest = 0
        boats = 0

        while heaviest > lightest:
            if people[heaviest] + people[lightest] <= limit:
                boats += 1
                heaviest -= 1
                lightest += 1
            else:
                boats += 1
                heaviest -= 1
        if heaviest == lightest:
            boats += 1
        return boats
