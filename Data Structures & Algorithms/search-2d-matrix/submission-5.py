class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l = 0 
            r = len(matrix[0]) - 1
            while l <= r:
                m = (l + r) // 2
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] < target:
                    l = m + 1
                elif matrix[i][m] > target:
                    r = m - 1
        return False
        
