class Solution:
    def distributeCandies(self, candyType):
        type_len, res, mapping = len(candyType), 0, {}
        for i in range(type_len):
            if candyType[i] not in mapping:
                mapping[candyType[i]] = 1
                res += 1
        return res if res < type_len // 2 else type_len // 2

    def distributeCandies2(self, candyType):
        type_len = len(candyType) // 2
        type_set = set(candyType)
        return type_len if len(type_set) >= type_len else len(type_set)


if __name__ == '__main__':
    s = Solution()
    res = s.distributeCandies(
        [100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0])
    print(res)
