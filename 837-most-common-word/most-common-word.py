class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)

        word_frequency = defaultdict(int)
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^a-zA-Z]', ' ', paragraph)
        
        words = paragraph.split()
        for word in words:
            if word not in ban:
                word_frequency[word] += 1

        word_frequency.pop("", None)

        result = ""
        max_frequency = 0
        for word, frequency in word_frequency.items():
            if not result or frequency > word_frequency[result]:
                result = word

        return result