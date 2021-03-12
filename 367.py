class Solution:
    def isPerfectSquare(self, num):
        for i in range(1, 100000):
            if i**2 == num:
                return True
            elif i**2 > num:
                break
        return False

    def isPerfectSquare2(self, num):
        left, right = 1, num

        while left < right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1

        return left * left == num
