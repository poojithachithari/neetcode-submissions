class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in resmap:
               return [resmap[diff],i]
            resmap[nums[i]] = i
                
        

        