class CQueue:
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def appendTail(self, value: int) -> None:
        self.stack_a.append(value)

    def deleteHead(self) -> int:
        if self.stack_b:
            return self.stack_b.pop()

        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())

        return self.stack_b.pop() if self.stack_b else -1
