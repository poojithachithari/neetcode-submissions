class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #approch 1
        # new_nums = set(nums)
        # if len(nums) != len(new_nums):
        #     return True
        # return False

        #approch 2

        result = set()
        for i in nums:
            if i in result:
                return True
            result.add(i)
        return False
        


        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False       