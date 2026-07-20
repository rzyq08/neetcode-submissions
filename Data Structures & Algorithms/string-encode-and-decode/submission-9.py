class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        return ''.join([f"{len(c)}#{c}" for c in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            end = j+1+length
            res.append(s[j+1:end])
            i = end
        return res