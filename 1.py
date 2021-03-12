class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


if __name__ == '__main__':
    nums = []
    nums.append(3)
    nums.append(2)
    nums.append(4)
    for i in range(len(nums)):
        print(i)
