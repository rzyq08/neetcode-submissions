class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        prefix = [1] * (length+1)
        postfix = [1] * (length+1)

        prefix[1] = nums[0]
        for i in range(1, length):
            prefix[i+1] = nums[i] * prefix[i]
        for i in range(length-1, -1, -1):
            postfix[i] = nums[i] * postfix[i+1]

        result = [1] * length
        for i in range(1, length+1):
            result[i-1] = prefix[i-1]*postfix[i]
        return result