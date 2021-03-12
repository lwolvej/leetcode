class Solution:
    def powerfulIntegers(self, x, y, bound):
        i, j, res = 1, 1, set()
        while i < bound:
            j = 1
            while i + j <= bound:
                res.add(i + j)
                if y == 1:
                    break
                j *= y
            if x == 1:
                break
            i *= x
        return list(res)
