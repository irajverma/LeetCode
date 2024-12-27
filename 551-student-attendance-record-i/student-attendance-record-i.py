class Solution:
    def checkRecord(self, s: str) -> bool:
        words=list(s)
        late_days='LLL'
        if words.count('A')<2 and late_days not in s:
            return True
        return False