class Solution:
    def hasGroupsSizeX(self, deck):
        mapping = {}
        for num in deck:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1
        res = 0
        for value in mapping.values():
            res = self.gcd(res, value)
        return res >= 2

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)