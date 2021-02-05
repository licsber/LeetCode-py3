from bisect import insort


class MedianFinder:

    def __init__(self):
        self.list = []

    def addNum(self, num: int) -> None:
        insort(self.list, num)

    def findMedian(self) -> float:
        L = len(self.list)
        return (self.list[L // 2] + self.list[(L - 1) // 2]) / 2
