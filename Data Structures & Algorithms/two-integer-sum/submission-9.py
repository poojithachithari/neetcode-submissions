class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #bruteforce 
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        res = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in res:
                return [res[diff],i]
            res[nums[i]] = i 

        