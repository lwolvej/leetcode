import heapq


class Solution:
    def lastStoneWeight(self, stones):
        stones = [-v for v in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            mm = heapq.heappop(stones)
            nn = heapq.heappop(stones)
            if mm != nn:
                heapq.heappush(stones, mm - nn)
        if stones:
            return -stones[0]
        else:
            return 0


if __name__ == '__main__':
    res = [1, 2, 3, 4, 5]
    res = [-v for v in res]
    heapq.heapify(res)
    print(res)
