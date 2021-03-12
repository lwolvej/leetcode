class Solution:
    def climbStairs(self, n: int):
        if n <= 2:
            return n
        res = 2
        pre = 1
        for i in range(3, n + 1):
            tmp = res
            res += pre
            pre = tmp
        return res