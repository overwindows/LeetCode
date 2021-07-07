class MaxQueue:

    def __init__(self):
        self.queue = []
        self.max_q = []

    def max_value(self) -> int:
        if self.queue:
            return self.max_q[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.max_q:
            if value > self.max_q[-1]:
                self.max_q.pop()
            else:
                break
        self.max_q.append(value)

    def pop_front(self) -> int:
        if self.queue:
            x = self.queue.pop(0)
            if x == self.max_q[0]:
                self.max_q.pop(0)
            return x
        else:
            return -1



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()