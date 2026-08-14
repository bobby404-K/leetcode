class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_of = {}
        for i, row in enumerate(["qwertyuiop", "asdfghjkl", "zxcvbnm"]):
            for ch in row:
                row_of[ch] = i
        
        result = []
        for word in words:
            lw = word.lower()
            if len(set(row_of[ch] for ch in lw)) == 1:
                result.append(word)
        
        return result