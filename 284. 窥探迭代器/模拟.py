class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.cache = None

    def peek(self):
        if self.cache is None:
            self.cache = self.iter.next()

        return self.cache

    def next(self):
        res = self.cache
        if self.cache is None:
            res = self.iter.next()

        if self.iter.hasNext():
            self.cache = self.iter.next()
        else:
            self.cache = None

        return res

    def hasNext(self):
        if self.cache is not None:
            return True

        return self.iter.hasNext()
