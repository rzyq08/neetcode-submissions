class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = {}
        for num in nums:
            count[num] = count.get(num, 0)+1
        
        for key,val in count.items():
            bucket[val].append(key)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res