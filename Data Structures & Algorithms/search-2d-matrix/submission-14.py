class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        # binary search on the row
        # binary search on the col

        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] == target:
                return True
            elif target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][0]:
                if target in matrix[m]:
                    return True 
                l = m + 1
        print(matrix[m])
        l = 0
        r = len(matrix[m]) - 1

        while l <= r:
            m_2 = l + (r - l) // 2
            print(matrix[m][m_2])
            if matrix[m][m_2] == target:
                return True
            elif target < matrix[m][m_2]:
                r = m_2 - 1
            elif target > matrix[m][m_2]: 
                l = m_2 + 1
        return False
            