class Solution:
    def findComplement(self, num):
        return int(bin(num)[2:].replace('0', '2').replace('1', '0').replace('2', '1'), 2)


if __name__ == '__main__':
    s = Solution()
    res = s.findComplement(5)
    print(res)
