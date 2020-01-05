#Min Stack
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/98/design/562/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []
        self.mins = []
        

    def push(self, x: int) -> None:
        if len(self.mins) == 0 or x < self.mins[-1]:
            self.mins.append(x)
        else:
            self.mins.append(self.mins[-1])
        self.vals.append(x)
        

    def pop(self) -> None:
        self.mins.pop()
        return self.vals.pop()
        

    def top(self) -> int:
        return self.vals[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
