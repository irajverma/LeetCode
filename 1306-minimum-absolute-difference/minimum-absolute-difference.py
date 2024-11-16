class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        arr.sort() 
        result = [] 

        min_diff = arr[1] - arr[0]

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff: 
                min_diff = diff
                result = [[arr[i - 1], arr[i]]] 
            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result