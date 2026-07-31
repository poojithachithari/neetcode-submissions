class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resMap=defaultdict()
        x=1
        for i in range(len(nums)):
            
            for j in range(len(nums)):
                if j == i:
                    continue
                x *= nums[j]
            resMap[i]= x
            x=1
        return list(resMap.values())




        