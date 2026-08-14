class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def canFinish(k):
            hours = 0
            for p in piles:
                hours += (p+k-1) //k
            return hours <= h


        while low<high:
            mid = (low + high)//2
            if canFinish(mid):
                high = mid 
            else:
                low = mid +1
        return low
        
        