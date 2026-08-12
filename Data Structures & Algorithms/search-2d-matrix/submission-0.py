class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (rows * cols) -1

        while left <= right:
            mid = (left+right) //2

            row = mid // cols
            col = mid %  cols
            middle_value = matrix[row][col]

            if middle_value == target:
                return True
            elif middle_value < target:
                left = mid + 1
            else:
                right = mid -1
        return False
        
        