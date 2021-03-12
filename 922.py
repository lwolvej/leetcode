class Solution:
    def sortArrayByParityII(self, nums):
        nums_len = len(nums)
        for i in range(nums_len):
            if i % 2 == 0:
                if nums[i] % 2 != 0:
                    for j in range(i, nums_len):
                        if nums[j] % 2 == 0:
                            nums[i], nums[j] = nums[j], nums[i]
                            break
            else:
                if nums[i] % 2 == 0:
                    for j in range(i, nums_len):
                        if nums[j] % 2 != 0:
                            nums[i], nums[j] = nums[j], nums[i]
                            break
        return nums

    def sortArrayByParityII2(self, nums):
        q, o, res = [], [], []
        for num in nums:
            if num % 2 == 0:
                o.append(num)
            else:
                q.append(num)
        for i in range(len(q)):
            res.append(o[i])
            res.append(q[i])
        return res
