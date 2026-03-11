class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.dq = deque()
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size < self.max_size:
            self.dq.appendleft(value)
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.max_size:
            self.dq.append(value)
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.size > 0:
            self.dq.popleft()
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size > 0:
            self.dq.pop()
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        val = -1
        if self.size > 0:
            val = self.dq[0]
            return val
        return val

    def getRear(self) -> int:
        val = -1
        if self.size > 0:
            val = self.dq[-1]
            return val
        return val

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.max_size:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()