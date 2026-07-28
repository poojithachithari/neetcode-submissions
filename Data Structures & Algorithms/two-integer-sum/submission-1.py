class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            return
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]

        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[i] <= target:
        #             x = target - nums[i]
        #             index = nums.index(x)
        #             return [i,index] 