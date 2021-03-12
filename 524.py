class Solution:
    def findLongestWord(self, s, d):
        d.sort(key=lambda v: (-len(v), v))
        for word in d:
            begin = 0
            for c in word:
                begin = s.find(c, begin) + 1
                if not begin:
                    break
            if begin:
                return word
        return ''


if __name__ == '__main__':
    s = Solution()
    res = s.findLongestWord("aewfafwafjlwajflwajflwafj", [
                            "apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"])
    print(res)
