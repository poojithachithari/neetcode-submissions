class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        max_area = 0
        while left <right:
            #area = distance * height
            #distance = right-left
            #height = min(hieght1,height2)
            distance = right-left
            height = min(heights[left],heights[right])
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            area = distance * height

            max_area = max(max_area,area)
            
        return max_area
        