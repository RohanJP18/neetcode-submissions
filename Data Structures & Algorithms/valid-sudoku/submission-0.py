class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         
        seen_c = {} # [1,2,3,4,5,6,7,8: [values],9: [values]]
        for i in range(9):
            seen_c[i] = set()
        seen_3_3 = {} # [1: 1, 2,. ; 2: .,3,. ; 3: .,.,. ]
        for i in range(9):
            seen_3_3[i] = set()

        for index_r in range(9): #row
            seen_r = {} # [1,2,3,4,.,5]
            for index_c in range(9): #col
                index_3_3 = (index_r // 3) * 3 + (index_c // 3)
                val = board[index_r][index_c]
                if val == ".":
                    continue
                if val in seen_r:
                    return False
                seen_r[val] = index_r
                if val in seen_c[index_c]:
                    return False
                seen_c[index_c].add(val)
                if val in seen_3_3[index_3_3]:
                    return False
                seen_3_3[index_3_3].add(val)

        return True
            


