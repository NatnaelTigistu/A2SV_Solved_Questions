class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        opr = 0
        while target != 1:
            if target == 2:
                opr += 1
                target = 1
            elif target % 2 == 0:
                if maxDoubles > 0:
                    opr += 1
                    maxDoubles -= 1
                    target = target//2 
                else:
                    return opr + target - 1
            else:
                opr += 1
                target -= 1
                if maxDoubles > 0:
                    opr += 1
                    maxDoubles -= 1
                    target = target//2
                else:
                    return opr + target - 1
        return opr