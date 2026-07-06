class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for item in strs:
            sort = ''.join(sorted(item))
            result[sort].append(item)

        return list(result.values())