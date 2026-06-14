class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns =defaultdict(set)
        grid = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                grid_key = (i//3, j//3)
                num = board[i][j]
                if num == '.': continue
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in grid[grid_key]:
                    return False
                rows[i].add(num)
                columns[j].add(num)
                grid[grid_key].add(num)
        return True