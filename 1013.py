class Solution:
    def canThreePartsEqualSum(self, arr):
        sum_arr = sum(arr)
        if sum_arr % 3 != 0:
            return False

        avg, cnt, tmp = sum_arr // 3, 0, 0
        for i in range(len(arr) - 1):
            tmp += arr[i]
            if tmp == avg:
                tmp = 0
                cnt += 1
            if cnt == 2:
                return True
        return False
