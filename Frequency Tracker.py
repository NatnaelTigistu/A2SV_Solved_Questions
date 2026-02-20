class FrequencyTracker:

    def __init__(self):
        self.count = {}   
        self.freq = {}    

    def add(self, number: int) -> None:
        old_count = self.count.get(number, 0)
        new_count = old_count + 1
        
        self.count[number] = new_count
        
        if old_count > 0:
            self.freq[old_count] -= 1

        self.freq[new_count] = self.freq.get(new_count, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.count or self.count[number] == 0:
            return
        
        old_count = self.count[number]
        new_count = old_count - 1
        
        self.count[number] = new_count
        
        self.freq[old_count] -= 1
        
        if new_count > 0:
            self.freq[new_count] = self.freq.get(new_count, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency, 0) > 0

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)