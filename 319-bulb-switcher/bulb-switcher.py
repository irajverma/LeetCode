class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        c,i=0,1
        while i*i <=n:
            c+=1
            i+=1
        return c