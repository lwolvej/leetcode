# TODO
class Solution:
    def minSubArrayLen(self, target, nums):
        i, sum_num, now_len, nums_len = 0, 0, 0, len(nums)
        for j in range(nums_len):
            sum_num += nums[j]
            while sum_num >= target:
                now_len = j - i + 1 if now_len == 0 else min(now_len, j - i + 1)
                sum_num -= nums[i]
                i += 1
        return now_len



if __name__ == '__main__':
    s = Solution()
    res = s.minSubArrayLen(5, [2,3,1,1,1,1,1])
    print(res)
