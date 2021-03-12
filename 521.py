class Solution:
    def findLUSlength(self, a, b):
        return -1 if a == b else max(len(a), len(b))


if __name__ == '__main__':
    s = Solution()
    res = s.findLUSlength('aba', 'caba')
    print(res)
