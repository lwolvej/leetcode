class Solution:
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        # 超时
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0, 0]
        elif (tomatoSlices == 0 and cheeseSlices != 0) or (tomatoSlices != 0 and cheeseSlices == 0):
            return []
        elif (tomatoSlices % 2 != 0) or (tomatoSlices < cheeseSlices * 2) or (tomatoSlices > cheeseSlices * 4):
            return []
        else:
            for i in range(cheeseSlices):
                j = cheeseSlices - i
                if i * 4 + j * 2 == tomatoSlices:
                    return [i, j]
            return []

    def numOfBurgers2(self, tomatoSlices, cheeseSlices):
        if tomatoSlices % 2 != 0 or tomatoSlices > 4 * cheeseSlices or tomatoSlices < 2 * cheeseSlices:
            return []
        a = (4 * cheeseSlices - tomatoSlices) // 2
        return [cheeseSlices - a, a]

# # 1   2
# 2 14
# 4 12
#
#
#
