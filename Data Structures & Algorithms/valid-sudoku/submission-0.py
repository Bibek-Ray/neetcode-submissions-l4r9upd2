from collections import defaultdict

class Solution:
    def checkDuplicate(self, nums: dict) -> int:
        
        for val in nums.values():
            seen = set()
            for a in val:
                if a in seen:
                    return 0
                    break
                else:
                    seen.add(a)
        
        return 1
                
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        sparse_matrix = {}
        row, col, box = defaultdict(list), defaultdict(list), defaultdict(list)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    sparse_matrix[(i, j)] = board[i][j]
        for key, val in sparse_matrix.items():
            row[key[0]].append(val)
            col[key[1]].append(val)
            box[(key[0]//3, key[1]//3)].append(val)
            
        flag = self.checkDuplicate(row) * self.checkDuplicate(col) * self.checkDuplicate(box)
        
        if flag == 0:
            return False
        else: 
            return True