class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        res = '' 
        count = 1
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                count+=1
            else:
                count = 1
            if count == 3:
                res = max(res, num[i] * 3)
                
        return res