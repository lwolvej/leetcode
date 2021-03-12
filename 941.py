class Solution:
    def validMountainArray(self, arr):
        if len(arr) <= 1:
            return False
        is_up, is_down, pre = False, False, arr[0]
        for i in range(1, len(arr)):
            if i != 1 and arr[i] < pre and (not is_up):
                is_up = True
                is_down = True
            if is_up:
                if arr[i] >= pre:
                    return False
            else:
                if arr[i] <= pre:
                    return False
            pre = arr[i]
        return is_down
