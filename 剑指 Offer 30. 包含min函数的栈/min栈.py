class MinStack:
    def __init__(self):
        self.stack = []
        self.help_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.help_stack:
            self.help_stack.append(x)
        else:
            top = self.help_stack[-1]
            self.help_stack.append(x if x < top else top)

    def pop(self) -> None:
        self.help_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.help_stack[-1]
