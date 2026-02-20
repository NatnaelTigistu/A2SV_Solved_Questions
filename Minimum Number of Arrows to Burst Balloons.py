class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points :
            return 0

        points = sorted(points,key = lambda x : (x[0],x[1]))
        arrows = 1

        i = 1
        currentBallonEnd = points[0][1]
        while i < len(points):
            if points[i][0] <= currentBallonEnd:
                if points[i][1] < currentBallonEnd:
                    currentBallonEnd = points[i][1]
                i += 1
            else: 
                arrows += 1
                currentBallonEnd = points[i][1]
        
        return arrows