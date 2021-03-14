import heapq


class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        heap = []
        for pass_, total_ in classes:
            heapq.heappush(
                heap, (pass_ / total_ - (pass_ + 1) / (total_ + 1), pass_, total_))
        while extraStudents > 0:
            _, pass_, total_ = heapq.heappop(heap)
            heapq.heappush(heap, ((pass_ + 1) / (total_ + 1) -
                                  (pass_ + 2) / (total_ + 2), pass_ + 1, total_ + 1))
            extraStudents -= 1
        heap_len, res = len(heap), 0
        for _, pass_, total_ in heap:
            res += pass_ / total_
        return res / heap_len
