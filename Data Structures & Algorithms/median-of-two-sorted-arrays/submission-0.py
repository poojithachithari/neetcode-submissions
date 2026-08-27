class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m,n = len(nums1),len(nums2)
        low,high = 0,m

        while low <= high:
            part1 = (low+high) //2
            part2 = (m+n+1)//2 -part1

            left1 = nums1[part1-1] if part1 > 0 else -1000000000
            right1 = nums1[part1] if part1 < m else 1000000000

            left2 = nums2[part2-1] if part2 >0 else -1000000000
            right2 = nums2[part2] if part2 < n else 1000000000

            if left1 <= right2 and left2 <= right1:
                if(m+n)%2 ==0:
                    return (max(left1,left2)+ min(right1,right2))/2.0
                else:
                    return max(left1,left2) *1.0
            elif left1 > right2:
                high = part1 -1
            else:
                low = part1+1
        


        