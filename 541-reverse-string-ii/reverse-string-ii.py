class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) == 1:
            return s
        else:
            flag = 1
            i=k
            r=s[k-1::-1]
            while i<len(s):
                if flag == 0:
                    r += s[i+k-1:i-1:-1]
                    flag = 1
                elif flag == 1:
                    r += s[i:i+k]
                    flag = 0
                i += k
            return r