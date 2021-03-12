class Solution:
    def fib(self, n):
        if n < 2:
            return n
        p, pp, now = 1, 0, 0
        while n > 1:
            now = p + pp
            pp = p
            p = now
            n -= 1
        return now


if __name__ == '__main__':
    s = Solution()
    res = s.fib(3)
    print(res)
