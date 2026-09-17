class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) #3
        cols = len(matrix[0]) #4

        left = 0 
        right = cols * rows - 1

        while left <= right:
            mid = (left + right) // 2 # initial mid = 5

            row = mid // cols #row = 1
            col = mid % cols

            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False