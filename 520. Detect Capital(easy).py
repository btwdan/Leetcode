class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0] >= 'a' and word[0] <= 'z':
            return word == word.lower()
        if word[0] >= 'A' and word[0] <= 'Z':
            if word == word.upper():
                return True
            else:
                return word[1:len(word)] == word[1:len(word)].lower()