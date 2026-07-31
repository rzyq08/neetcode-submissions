class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        mx = 0
        for n in num:
            if n-1 not in num:
                count=0
                while n+count in num:
                    count+=1
                mx = max(mx, count)
        return mx