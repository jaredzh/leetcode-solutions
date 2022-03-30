class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n
        
        while left < right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        row, col = left // n, left % n
        if row >= m or col >= n:
            return False
        return matrix[row][col] == target