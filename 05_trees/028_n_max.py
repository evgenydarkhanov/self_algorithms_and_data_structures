# найти n-ый наибольший поступающий элемент (в потоке?)
# [1, 2, 3, 4, 5, 6, 7, 8], 3 --> 6
# [1, 2, 3, 4, 5, 6, 7, 8], 1 --> 8
# [1, 2, 3, 4, 5, 6, 7, 8], 8 --> 1
# можно создать кучу и добавлять в неё

import heapq
from typing import Optional


class NLarge:
    def __init__(self, n):
        self.n = n
        self.h = []

    def add(self, elem) -> Optional[int]:
        heapq.heappush(self.h, elem)

        if len(self.h) >= self.n:
            while len(self.h) > self.n:
                heapq.heappop(self.h)
            return self.h[0]
        return None


if __name__ == "__main__":
    nl = NLarge(3)

    assert nl.add(1) is None
    assert nl.add(2) is None
    assert nl.add(3) == 1
    assert nl.add(4) == 2
    assert nl.add(10) == 3
