class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        
        result = []
        for word in words:
            lower_word = set(word.lower())
            for row in rows:
                if lower_word <= row:
                    result.append(word)
                    break
        
        return result