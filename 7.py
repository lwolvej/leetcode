import sys


class Solution:
    def reverse(self, x):
        bok = x >= 0
        res = int(str(abs(x))[::-1])
        res = res if bok else -1*res
        return res if -2**31 < res < 2**31-1 else 0


if __name__ == '__main__':
    s = Solution()
    res = s.reverse(-321)
    print(res)
