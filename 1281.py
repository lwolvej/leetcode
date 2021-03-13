class Solution:
    def subtractProductAndSum(self, n):
        jj, hh = 1, 0
        while n != 0:
            tmp = n % 10
            n //= 10
            jj *= tmp
            hh += tmp
        return jj - hh 
    
    def subtractProductAndSum2(self, n):
        jj, hh = 1, 0
        for i in str(n):
            jj *= int(i)
            hh += int(i)
        return jj - hh