class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.cache = self.iter.next()
        self.has_next = self.iter.hasNext()

    def peek(self):
        return self.cache

    def next(self):
        res = self.cache
        self.has_next = self.iter.hasNext()
        self.cache = self.iter.next() if self.has_next else None
        return res

    def hasNext(self):
        return self.has_next
