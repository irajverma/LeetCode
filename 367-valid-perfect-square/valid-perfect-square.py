class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        q = num // 4  # Integer division in Python
        i = 1
        while i * i <= num:  # Check if i*i exceeds num
            if i * i == num:
                return True
            i += 1
        return False