class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        res = []
        for item in strs:
            res.append(str(len(item)))
            res.append('#')
            res.append(item)
        return ''.join(res)

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