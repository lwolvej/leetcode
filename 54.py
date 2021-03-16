class Solution:
    def spiralOrder(self, matrix):
        res = []
        i, j, now, r, nn = 0, 0, 0, 0, 0
        x_len, y_len = len(matrix), len(matrix[0])
        num = x_len * y_len
        while nn != num:
            res.append(matrix[i][j])
            nn += 1
            if now == 0:
                if j == y_len - 1 - r:
                    now += 1
                    i += 1
                else:
                    j += 1
            elif now == 1:
                if i == x_len - 1 - r:
                    now += 1
                    j -= 1
                else:
                    i += 1
            elif now == 2:
                if j == r:
                    now += 1
                    i -= 1
                    r += 1
                else:
                    j -= 1
            else:
                if i == r:
                    now = 0
                    j += 1
                else:
                    i -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(res)
