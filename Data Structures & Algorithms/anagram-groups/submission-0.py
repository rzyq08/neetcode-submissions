class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        lst = []

        for item in strs:
            sort = ''.join(sorted(item))
            result[sort].append(item)

        for key, val in result.items():
            lst.append(val)

        return lst