class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        total, val, left = 1, x, abs(n)

        while left > 1:
            if left % 2 == 0:
                left = left // 2
                val = val * val
            else:
                total *= val
                left -= 1
        if n > 0:
            return total * val
        else:
            return 1/(total * val)
