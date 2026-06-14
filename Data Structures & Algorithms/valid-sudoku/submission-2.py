class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]* 9
        columns =[0]* 9
        grid = [0]* 9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                num = int(board[i][j])
                mask = 1 << num 
                grid_key = (i//3)*3+(j//3)

                
                if ( rows[i] & mask 
                    or columns[j] & mask 
                    or grid[grid_key] & mask ):
                    return False
                
                rows[i] |= mask 
                columns[j] |= mask
                grid[grid_key] |= mask

        return True