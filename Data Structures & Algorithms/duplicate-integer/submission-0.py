class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist = set()
        for i in range(len(nums)):
            if nums[i] in newlist:
                return True
            newlist.add(nums[i])
        return False



        