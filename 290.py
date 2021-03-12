class Solution:
    def wordPattern(self, pattern, s):
        pattern_len = len(pattern)
        book = [False for _ in range(pattern_len)]
        ss = s.split(' ')
        if pattern_len != len(ss):
            return False
        mapping = {}
        for i in range(pattern_len):
            if not book[i]:
                if ss[i] in mapping:
                    return False
                j = i
                book[i] = True
                mapping[ss[i]] = 1
                while j < pattern_len:
                    if pattern[j] == pattern[i]:
                        if ss[j] != ss[i]:
                            return False
                        else:
                            book[j] = True
                    j += 1
        return True


if __name__ == '__main__':
    s = Solution()
    res = s.wordPattern("abba", "dog dog dog dog")
    print(res)
