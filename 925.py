class Solution:
    def isLongPressedName(self, name, typed):
        if name == typed:
            return True
        name_len, typed_len = len(name), len(typed)
        if name_len == typed_len:
            return False
        typed_now, i = 0, 0
        while i < name_len:
            num, num1 = 0, 0
            while i + num < name_len and name[i + num] == name[i]:
                num += 1
            while typed_now < typed_len:
                if name[i] == typed[typed_now]:
                    num1 += 1
                    typed_now += 1
                else:
                    break
            if num1 < num:
                return False
            i += num
        return typed_now == typed_len
