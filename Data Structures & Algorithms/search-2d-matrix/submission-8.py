class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, left, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1

        while top <= bottom:
            mid_v = (top + bottom)//2
            if target > matrix[mid_v][-1]:
                top = mid_v + 1
            elif target < matrix[mid_v][0]:
                bottom = mid_v - 1
            else:
                break
        while left <= right:
            mid_h = (left + right)//2
            if target > matrix[mid_v][mid_h]:
                left = mid_h + 1
            elif target < matrix[mid_v][mid_h]:
                right = mid_h - 1
            else:
                return True
        
        return False
            