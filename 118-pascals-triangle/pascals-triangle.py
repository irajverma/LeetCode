class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for row in range(1, numRows+1):
            res= 1
            temp = [res]
            for col in range(1, row):
                res = res * (row-col)
                res = res // col
                temp.append(res)
            ans.append(temp)
        return ans