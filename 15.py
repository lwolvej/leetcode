class Solution:
    def threeSum(self, nums):
        nums_len = len(nums)
        if nums_len < 3:
            return []
        nums = sorted(nums)
        res = []
        for i in range(nums_len - 1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            begin, end = i + 1, nums_len - 1
            while begin < end:
                tmp_sum = nums[begin] + nums[end] + nums[i]
                if tmp_sum > 0:
                    end -= 1
                elif tmp_sum < 0:
                    begin += 1
                else:
                    res.append([nums[i], nums[begin], nums[end]])
                    while begin < end and nums[begin] == nums[begin + 1]:
                        begin += 1
                    while begin < end and nums[end] == nums[end - 1]:
                        end -= 1
                    begin += 1
                    end -= 1
        return res


if __name__ == '__main__':
    for i in range(1, 10):
        print(i)
        if i == 5:
            continue
