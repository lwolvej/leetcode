class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda e: (e[0], e[1]))
        intervals_len, i = len(intervals), 0
        res = []
        while i < intervals_len:
            tmp = intervals[i]
            j = i + 1
            while j < intervals_len and intervals[j][0] <= tmp[1]:
                tmp[0] = min(tmp[0], intervals[j][0])
                tmp[1] = max(tmp[1], intervals[j][1])
                j += 1
            i = j
            res.append(tmp)
        return res
