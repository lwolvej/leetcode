class Solution:
    def generateMatrix(self, n):
        res = [[0 for _ in range(n)] for _ in range(n)]
        i, j, now, r, direct = 0, 0, 0, 0, 0
        num = n**2
        while now != num:
            res[i][j] = now + 1
            now += 1
            if direct == 0:
                if j == n - 1 - r:
                    i += 1
                    direct += 1
                else:
                    j += 1
            elif direct == 1:
                if i == n - 1 - r:
                    j -= 1
                    direct += 1
                else:
                    i += 1
            elif direct == 2:
                if j == r:
                    i -= 1
                    direct += 1
                    r += 1
                else:
                    j -= 1
            else:
                if i == r:
                    j += 1
                    direct = 0
                else:
                    i -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.generateMatrix(1)
    print(res)
