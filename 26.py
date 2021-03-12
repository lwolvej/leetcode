class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i, k, book = 0, 1, nums[0]
        while i < len(nums):
            if nums[i] != book:
                nums[k] = nums[i]
                book = nums[k]
                k += 1
            i += 1
        return k
        

        
if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    res = s.removeDuplicates(nums)
    print(res)
    print(nums)