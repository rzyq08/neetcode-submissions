class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            trgt = target - num
            if trgt in seen:
                return [seen[trgt], i]

            seen[num] = i