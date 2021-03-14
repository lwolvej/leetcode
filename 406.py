class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda e: (-e[0], e[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
