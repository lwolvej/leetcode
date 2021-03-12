class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False
        if num <= 3:
            return True
        nums = [2, 3, 5]
        while num != 1:
            tag = True
            for i in range(3):
                if num % nums[i] == 0:
                    num /= nums[i]
                    tag = False
            if tag and (num not in nums):
                return False
        return True
    
    def isUgly2(self, num):
        if num <= 0:
            return False
        while not num % 2:
            num >>= 1
        while not num % 3:
            num //= 3
        while not num % 5:
            num //= 5
        return num == 1

if __name__ == '__main__':
    s = Solution()
    res = s.isUgly(14)
    print(res)

                
            