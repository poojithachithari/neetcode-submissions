class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left  = 0
        right = len(heights)-1
        maxarea = 0
        while left<right:
            #area = distance*height

            min_height = min(heights[left],heights[right])

            dist = right-left

            area = dist*min_height
            maxarea = max(maxarea,area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxarea
        