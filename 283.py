class Solution:
    def moveZeroes(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    s = Solution()
    res = [0, 1, 0, 3, 12]
    s.moveZeroes(res)
    print(res)
