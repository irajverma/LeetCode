class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows<=1:
            return [[1]]
        nums=[[1]]
        for i in range(1,numRows):
            newnum=[1]
            for j in range(len(nums[i-1])-1):
                newnum.append(nums[i-1][j]+nums[i-1][j+1])
            newnum.append(1)
            nums.append(newnum)
        return nums