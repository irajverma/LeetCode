class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = 0
        if x < 0:
            is_negative = 1
            x = -x  

        reverse=0
        while (x>0):
            a=x%10
            reverse = reverse * 10 + a
            x=x//10

        if is_negative:
            reverse = -reverse
        
        if reverse < -2147483648 or reverse > 2147483647:
            return 0
            
        return (reverse)