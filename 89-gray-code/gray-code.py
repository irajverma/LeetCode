class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        k = 2**n-1
        lt = [0]
        x=0
        while(x<n):
            p = len(lt)
            two = 2**x
            for i in range(p-1, -1, -1):
                lt.append(two | lt[i])
            x+=1
        return lt