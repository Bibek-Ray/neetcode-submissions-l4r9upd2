class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, left, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1

        while top <= bottom:
            mid_v = (top + bottom)//2
            if target > matrix[mid_v][-1]:
                top += 1
            elif target < matrix[mid_v][-1]:
                bottom -= 1
            else:
                return True
        while left <= right:
            mid_h = (left + right)//2
            if target > matrix[mid_v][mid_h]:
                left += 1
            elif target < matrix[mid_v][mid_h]:
                right -= 1
            else:
                return True
        
        return False
            