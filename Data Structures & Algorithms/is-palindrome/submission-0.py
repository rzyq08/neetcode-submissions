class Solution:
    def isPalindrome(self, s: str) -> bool:
        before = [let.lower() for let in s if let.isalnum() == True]
        s = [let.lower() for let in s if let.isalnum() == True]

        left = 0
        right = len(s)-1
        for i in range((len(s)//2)):
            if left == right:
                break
            s[left], s[right] = s[right], s[left]
            left +=1
            right -=1
        return before == s