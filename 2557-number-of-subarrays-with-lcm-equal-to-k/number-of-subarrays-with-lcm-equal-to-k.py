class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def find_lcm(a, b):
            return abs(a * b) // gcd(a, b)
        c=0
        for i in range(len(nums)):
            l=nums[i]
            if l==k:
                c+=1
            if l>k:
                continue
            for j in range(i+1,len(nums)):
                l=find_lcm(l,nums[j])
                if l==k:
                    c+=1
                if l>k:
                    break
        return c



        