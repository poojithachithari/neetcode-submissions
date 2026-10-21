class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        new_nums = set(nums)
        if len(nums) != len(new_nums):
            return True
        return False


        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False       