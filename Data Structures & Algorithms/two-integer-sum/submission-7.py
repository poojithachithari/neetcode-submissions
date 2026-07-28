class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i,j]

        for i in range(len(nums)):
            x = target - nums[i]
            if x in result:
                return [result[x],i]
            result[nums[i]] = i
            
           
                
                        

                    