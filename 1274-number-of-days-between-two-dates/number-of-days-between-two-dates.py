class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        month_to_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        y1, m1, d1 = [int(i) for i in date1.strip().split("-")]
        y2, m2, d2 = [int(i) for i in date2.strip().split("-")]

        def get_days_until_1971(y, m, d):
            days = d
            for i in range(1, m):
                if i == 2 and y % 4 == 0 and y != 2100:
                    days += 29
                else:
                    days += month_to_days[i]
            
            for y in range(1971, y):
                if y % 4 == 0 and y != 2100:
                    print(y, 366)
                    days += 366
                else:
                    print(y, 365)
                    days += 365
            return days

        a = get_days_until_1971(y1, m1, d1)
        b = get_days_until_1971(y2, m2, d2)
        
        return b - a if b > a else a - b   