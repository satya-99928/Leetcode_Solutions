class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        row=[set() for _ in range(n)]
        col=[set() for _ in range(n)]
        box=[set() for _ in range(n)]
        for r in range(n):
            for c in range(n):
                val=board[r][c]
                if val==".":
                    continue
                box_idx=(r//3)*3+(c//3)
                if val in row[r] or val in col[c] or val in box[box_idx]:
                    return False
                row[r].add(val)
                col[c].add(val)
                box[box_idx].add(val)
        return True

        