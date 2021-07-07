class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.length = 0


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.length += 1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.length -= 1
        for i in range(self.length):
            x = self.queue.pop(0)
            self.queue.append(x)
        x = self.queue.pop(0)
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[self.length-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.length == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()