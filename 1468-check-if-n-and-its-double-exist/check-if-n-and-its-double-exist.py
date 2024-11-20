class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]==2*arr[i] or arr[i]==2*arr[j]:
                    return True
        return  False