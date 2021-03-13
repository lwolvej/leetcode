from collections import Counter


class Solution:
    def findSpecialInteger(self, arr):
        arr_len = len(arr)
        num, now = arr_len // 4, 0
        pre = arr[0]
        for i in range(1, arr_len):
            if arr[i] == pre:
                now += 1
                if now > num:
                    return pre
            else:
                now = 0
                pre = arr[i]
        return pre

    def findSpecialInteger2(self, arr):
        target = len(arr) // 4
        dd = Counter(arr)
        for i, v in dd.items():
            if v > target:
                return i
        return arr[0]
