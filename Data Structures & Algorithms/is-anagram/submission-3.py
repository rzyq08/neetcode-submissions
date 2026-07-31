class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        if length != len(t):
            return False

        alph = [0]*26
        for i in range(length):
            alph[ord(s[i])-ord('a')]+=1
            alph[ord(t[i])-ord('a')]-=1
        
        for num in alph:
            if num!=0:
                return False
        return True