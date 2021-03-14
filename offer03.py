import collections

class Solution:
    def findRepeatNumber(self, nums):
        return collections.Counter(nums).most_common(1)[0][0]

    def findRepeatNumber2(self, nums):
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
        for k, v in mapping.items():
            if v > 1:
                return k


if __name__ == '__main__':
    s = Solution()
    res = s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3, 3, 3, 3, 3, 4])
    print(res)
