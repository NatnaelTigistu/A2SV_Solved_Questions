class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5 or bills[1] == 20 or bills[2] == 20:
            return False
        bills_coll = deque()
        for i in range(len(bills)):
            bill = bills[i]
            if bill == 10:
                if not bills_coll:
                    return False
                if bills_coll[0] != 5:
                    return False
                else:
                    bills_coll.popleft()
                    bills_coll.append(10)
            elif bill == 20:
                if not bills_coll:
                    return False
                if bills_coll[0] != 5:
                    return False
                else :
                    bills_coll.popleft()
                    if not bills_coll:
                        return False
                    if bills_coll[-1] == 10:
                        bills_coll.pop()
                    else:
                        bills_coll.pop()
                        if not bills_coll:
                            return False
                        bills_coll.pop()
            else:
                bills_coll.appendleft(bill)
         
        return True
