class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        rev = num[::-1]
        for i, x in enumerate(rev):
            if x != '0':
                break
        return num[0:len(num)-i]