import heapq


class Solution:
    def kClosest(self, points, k):
        mapping = {}
        for i, point in enumerate(points):
            dis = point[0]*point[0] + point[1]*point[1]
            if dis in mapping:
                mapping[dis].append(i)
            else:
                mapping[dis] = [i]
        mapping = dict(sorted(mapping.items(), key=lambda e: e[0]))
        res, n, tag = [], 0, False
        for nums in mapping.values():
            for num in nums:
                n += 1
                res.append(points[num])
                if n >= k:
                    tag = True
                    break
            if tag:
                break
        return res

    def kClosest2(self, points, k):
        q = [(-x*x-y*y, i) for i, (x, y) in enumerate(points[:k])]
        heapq.heapify(q)
        for i in range(k, len(points)):
            x, y = points[i]
            heapq.heappushpop(q, (-x*x-y*y, i))
        return [points[i] for (_, i) in q]


if __name__ == '__main__':
    s = Solution()
    res = s.kClosest([[1, 3], [-2, 2]], 1)
    print(res)
