class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        total_elm=m*n
        k=k%total_elm
        res=[[0]*n for _ in range(m)]
            
        for r in range(m):
            for c in range(n):
                old=r*n+c
                new=(old+k)%total_elm
                new_r=new//n
                new_c=new%n
                res[new_r][new_c]=grid[r][c]
        return res
        