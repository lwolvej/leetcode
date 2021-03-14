class Solution:
    def findCenter(self, edges) -> int:
        points = [0 for _ in range(100001)]
        point_set = set()
        for edge in edges:
            x, y = edge
            points[x] += 1
            points[y] += 1
            if x not in point_set:
                point_set.add(x)
            if y not in point_set:
                point_set.add(y)
        point_num = len(point_set)
        res = 0
        for pp in point_set:
            if points[pp] == point_num - 1:
                res = pp
                break
        return res
