import itertools

class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        word_1 = list(itertools.chain(*word1))
        word_2 = list(itertools.chain(*word2))

        len1 = len(word_1)
        len2 = len(word_2)
        
        if len1 != len2:
            return False
        
        for i in range(len1):
            if word_1[i] != word_2[i]:
                return False
        
        if word_1[-1] != word_2[-1]:
            return False
        
        return True
