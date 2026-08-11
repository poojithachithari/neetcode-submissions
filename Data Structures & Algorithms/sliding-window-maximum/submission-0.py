class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        dq = deque()

        l,r=0,0

        while r<n:

            #Remove smaller elements
            while dq and nums[r]>=nums[dq[-1]]:
                dq.pop()
            
            #Add Current Index
            dq.append(r)

            #Remove out of bound index out of window size
            if dq[0]<l:
                dq.popleft()
            
            #Add the result
            if r+1>=k:
                result.append(nums[dq[0]])
                l+=1
            r+=1
        return result
            
        
            

        