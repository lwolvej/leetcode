class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start < end:
            if not ('a' <= s[start] <= 'z' or '0' <= s[start] <= '9'):
                start += 1
                continue
            if not ('a' <= s[end] <= 'z' or '0' <= s[end] <= '9'):
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def isPalindrome2(self, s):
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()
    res = s.isPalindrome("0P")
    print(res)
