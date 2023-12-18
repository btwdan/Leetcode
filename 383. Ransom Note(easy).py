class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        slovar = {}
        for word in ransomNote:
            slovar[word] = ransomNote.count(word)

        for word in ransomNote:
            if slovar[word] >  magazine.count(word):
                return False

        return True