class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashM = defaultdict(int)

        for num in nums:
            hashM[num] += 1

        lst = []
        for i in range(k):
            mx = max(hashM, key=hashM.get)
            lst.append(mx)
            hashM[mx] = 0

        return lst