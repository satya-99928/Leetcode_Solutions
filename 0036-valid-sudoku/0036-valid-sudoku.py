class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        n=len(board)
        for r in range(n):
            for c in range(n):
                val=board[r][c]
                if val!=".":
                    row=f"row {r} has {val}"
                    col=f"col {c} has {val}"
                    box=f"box {r//3}-{c//3} has {val}"
                    if row in seen or col in seen or box in seen:
                        return False
                    seen.update([row,col,box])
        return True

        