class Solution:
    def isPalindrome(self, x):
        now = str(x)
        return now == now[::-1]

if __name__ == '__main__':
    s = Solution()
    res = s.isPalindrome(10)
    print(res)