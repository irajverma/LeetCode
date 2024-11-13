class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        pcounts = [0] * (len(words) + 1)
        
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                pcounts[i + 1] = pcounts[i] + 1
            else:
                pcounts[i + 1] = pcounts[i]
        
        return [pcounts[end + 1] - pcounts[start] for start, end in queries]