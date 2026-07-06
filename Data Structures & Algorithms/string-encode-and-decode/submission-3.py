class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        return ''.join(str(len(item))+'#'+item for item in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = 1+j
            j = i+length
            res.append(s[i:j])
            i = j
        return res 