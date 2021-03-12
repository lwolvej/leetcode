class Solution:
    def convertToTitle(self, n):
        res = ''
        while n > 0:
            n -= 1
            n, y = divmod(n, 26)
            res = chr(y + 65) + res
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.convertToTitle(701)
    print(res)
