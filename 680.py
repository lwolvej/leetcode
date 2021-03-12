class Solution:
    def validPalindrome(self, s):
        begin, end = 0, len(s) - 1
        while begin < end:
            if s[begin] != s[end]:
                return self.isValid(s, begin + 1, end) or self.isValid(s, begin, end - 1)
            begin += 1
            end -= 1
        return True

    def isValid(self, s, begin, end):
        while begin < end:
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True

    def validPalindrome2(self, s):
        if s == s[::-1]:
            return True
        begin, end = 0, len(s) - 1
        while begin < end:
            if s[begin] != s[end]:
                a = s[begin + 1:end + 1]
                b = s[begin:end]
                return a == a[::-1] or b == b[::-1]
            else:
                begin += 1
                end -= 1


if __name__ == '__main__':
    s = Solution()
    res = s.validPalindrome(
        "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
    print(res)
# cabadc
