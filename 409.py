import collections


class Solution:
    def longestPalindrome(self, s):
        mapping = {}
        for c in s:
            if c in mapping:
                mapping[c] = mapping[c] + 1
            else:
                mapping[c] = 1
        has_one, res = False, 0
        for value in mapping.values():
            if value % 2 == 1:
                if not has_one:
                    has_one = True
                res += value - 1
            else:
                res += value
        if has_one and res % 2 == 0:
            res += 1
        return res

    def longestPalindrome2(self, s):
        res, count = 0, collections.Counter(s)
        for v in count.values():
            res += v // 2 * 2
            if res % 2 == 0 and v % 2 == 1:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.longestPalindrome("abccccdd")
    print(res)
