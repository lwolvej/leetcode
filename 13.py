class Solution:
    def romanToInt(self, s):
        switch = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        size = len(s)
        index = 0
        res = 0
        while index < size:
            if s[index] == 'I':
                if index + 1 < size:
                    if s[index + 1] == 'V':
                        res += 3
                        index += 1
                    elif s[index + 1] == 'X':
                        res += 8
                        index += 1
                res += 1
            elif s[index] == 'X':
                if index + 1 < size:
                    if s[index + 1] == 'L':
                        res += 30
                        index += 1
                    elif s[index + 1] == 'C':
                        res += 80
                        index += 1
                res += 10
            elif s[index] == 'C':
                if index + 1 < size:
                    if s[index + 1] == 'D':
                        res += 300
                        index += 1
                    elif s[index + 1] == 'M':
                        res += 800
                        index += 1
                res += 100
            else:
                res += switch[s[index]]
            index += 1
        return res

    def romanToInt2(self, s):
        switch = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            res += switch[s[i]]
            if i >= 1 and switch[s[i]] > switch[s[i - 1]]:
                res -= 2*switch[s[i - 1]]
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.romanToInt2("IV")
    print(res)
