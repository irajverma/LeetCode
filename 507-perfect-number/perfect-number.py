class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 5:
            return False


        sum = 1        
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum += i + num // i

        return sum == num 