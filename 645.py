class Solution:
    def findErrorNums(self, nums):
        nums_len = len(nums)
        books = [False for _ in range(nums_len + 1)]
        res = []
        for num in nums:
            if books[num]:
                res.append(num)
            else:
                books[num] = True
        for i in range(1, nums_len + 1):
            if not books[i]:
                res.append(i)
                break
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.findErrorNums([1, 2, 2, 4])
    print(res)
