class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        i, k = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
    
if __name__ == '__main__':
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    res = s.removeElement(nums, 2)
    print(res)
    print(nums)
