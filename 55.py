class Solution:
    def canJump(self, nums):
        nums_len = len(nums)
        if nums_len <= 1:
            return True
        max_dis, i = nums[0], 1
        while i < nums_len - 1:
            if i <= max_dis:
                max_dis = max(max_dis, nums[i] + i)
            i += 1
        return max_dis >= nums_len

    def canJump2(self, nums):
        max_dis = 0
        for i, num in enumerate(nums):
            if i <= max_dis < i + num:
                max_dis = i + num
        return max_dis >= i


if __name__ == '__main__':
    s = Solution()
    res = s.canJump2([2, 3, 1, 1, 4])
    print(res)
