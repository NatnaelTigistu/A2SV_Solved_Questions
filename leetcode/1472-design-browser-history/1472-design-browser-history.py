class BrowserHistory:

    def __init__(self, homepage: str):
        self.forwards = []
        self.f = 0
        self.backward = [homepage]
        self.b = 0
    def visit(self, url: str) -> None:
        self.forwards.append(url)
        self.f = 0
        self.b += 1
        self.backward.append(url)

    def back(self, steps: int) -> str:
        while self.b > 0 and steps > 0:
            self.b -= 1
            self.f += 1
            steps -= 1
            self.forwards.append(self.backward.pop())        
        return self.backward[-1]
    def forward(self, steps: int) -> str:
        while self.f > 0 and steps > 0:
            self.b += 1
            self.f -= 1
            steps -= 1
            self.backward.append(self.forwards.pop())        
        return self.backward[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)