class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result=[]
        for i in range(left, right + 1):
            num = i

            while num:
                x = num % 10
                if x == 0:
                    break
                if i % x != 0:
                    break
                num //= 10

            if num == 0:
                result.append(i)

        return result