def mergeAlternately(self, word1: str, word2: str) -> str:
        new=""
        i=0
        while i < len(word1) and i < len(word2):
            new = new + word1[i] + word2[i]
            i +=1
        new = new + word1[i:]
        new = new+ word2[i:]
        return new
