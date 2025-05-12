class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def signFunc(x) :
            if (x > 0):
                return 1
            elif (x < 0):
                return -1
            else:
                return 0

        res = 1
        for i in nums:
            res *= i

        return signFunc(res)