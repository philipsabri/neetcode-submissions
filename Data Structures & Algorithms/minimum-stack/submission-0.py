class MinStack:

    def __init__(self):
        self.stack = []
        self.tracker = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.tracker.append(min(val, self.tracker[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.tracker.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.tracker[-1]

