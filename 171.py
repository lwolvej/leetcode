class Solution:
    def titleToNumber(self, s):
        res = 0
        for c in s:
            res *= 26
            res += ord(c) - ord('A') + 1
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.titleToNumber('ABCDEF')
    print(res)
