class Solution:
    def lemonadeChange(self, bills):
        now_5, now_10 = 0, 0
        for bill in bills:
            if bill == 5:
                now_5 += 1
            elif bill == 10:
                if now_5 < 1:
                    return False
                else:
                    now_10 += 1
                    now_5 -= 1
            elif bill == 20:
                if now_5 > 0:
                    if now_10 > 0:
                        now_5 -= 1
                        now_10 -= 1
                    elif now_5 > 2:
                        now_5 -= 3
                    else:
                        return False
                else:
                    return False

        return True
