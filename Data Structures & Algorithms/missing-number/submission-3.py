class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # My Solution
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

        #Real Solution
        res = len(nums)
        for i in range(len(nums)):
            res +=(i-nums[i])
        return res
        