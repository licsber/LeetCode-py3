from bisect import insort


class MedianFinder:

    def __init__(self):
        self.list = []

    def addNum(self, num: int) -> None:
        insort(self.list, num)

    def findMedian(self) -> float:
        l = len(self.list)
        return (self.list[l // 2] + self.list[(l - 1) // 2]) / 2
