class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        strs_len = len(strs)
        index = -1
        for i, c in enumerate(strs[0]):
            flag = True
            for j in range(1, strs_len):
                if i >= len(strs[j]) or c != strs[j][i]:
                    flag = False
                    break
            if flag:
                index = i
            else:
                break
        return strs[0][0:index+1]


if __name__ == '__main__':
    s = Solution()
    res = s.longestCommonPrefix(["flower","flow","flight"])
    print(res)