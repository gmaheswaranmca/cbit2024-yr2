def dfs(r,c,gdata): #BFS
    grid, rows, cols, visited = gdata
    stack = [ (r, c) ]
    while stack:
        qr, qc = stack.pop()
        if (qr,qc) in visited: #queue cell
            continue 
        visited.add(  (qr,qc)  ) #mark the cell         
        directions_offset = [(1,0),(-1,0),(0,1),(0,-1)] #check neighbours land #right,left,down,up 
        for roffset, coffset in directions_offset:
            nr, nc = (qr + roffset), (qc + coffset) #each neigbout cell
            isCellInRange = (0 <= nr <= rows-1) and (0 <= nc <= cols-1)
            if isCellInRange:
                isNonVisitedLand = (grid[nr][nc] == '1') and ( (nr,nc) not in visited )
            if isCellInRange and isNonVisitedLand:
                stack.append( (nr,nc) )
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        for r in range(rows):
            for c in range(cols): #each cell
                isNonVisitedLand = (grid[r][c] == '1') and ( (r,c) not in visited )
                if isNonVisitedLand:
                    gdata = (grid, rows, cols, visited)
                    dfs(r,c,gdata)
                    islands += 1 #if non visited land
        return islands