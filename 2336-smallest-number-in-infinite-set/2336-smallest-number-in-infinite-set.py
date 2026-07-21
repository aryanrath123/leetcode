import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.cur = 1
        self.heap = []
        self.seen = set()

    def popSmallest(self) -> int:
        if self.heap:
            x = heapq.heappop(self.heap)
            self.seen.remove(x)
            return x
        self.cur += 1
        return self.cur - 1

    def addBack(self, num: int) -> None:
        if num < self.cur and num not in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.add(num)