class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        m=[]
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]]=1
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for i in sorted_items[:k]:
            m.append(i[0])
        return m
