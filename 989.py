class Solution:
    def addToArrayForm(self, A, K):
        pre = False
        A = list(reversed(A))
        for i in range(len(A)):
            tmp = K % 10
            K //= 10
            if pre:
                A[i] += 1
            A[i] += tmp
            if A[i] >= 10:
                pre = True
                A[i] -= 10
            else:
                pre = False
        while K != 0:
            tmp = K % 10
            K //= 10
            if pre:
                tmp += 1
            if tmp >= 10:
                pre = True
                tmp -= 10
            else:
                pre = False
            A.append(tmp)
        if pre:
            A.append(1)
        return list(reversed(A))


