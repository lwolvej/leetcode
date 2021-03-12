class Solution:
    def repeatedNTimes(self, A):
        t = set()
        for a in A:
            if a in t:
                return a
            else:
                t.add(a)
