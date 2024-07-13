def dfs(r,c,letterIndex, gdata):
    board, word, rows, cols = gdata 
    if letterIndex == len(word):
        return True
    if (not (0 <= r < rows)) or (not(0 <= c < cols)) or board[r][c] != word[letterIndex]:
        return False 
    ch = board[r][c]
    board[r][c] = '#'
    #
    found = (
                dfs(r+1,c,letterIndex+1,gdata) or 
                dfs(r-1,c,letterIndex+1,gdata) or 
                dfs(r,c+1,letterIndex+1,gdata) or 
                dfs(r,c-1,letterIndex+1,gdata)
            )   #right, left, down, up for next character
    board[r][c] = ch 
    return found 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                gdata = (board, word, rows, cols)
                if dfs(r,c,0,gdata): #cell, letter index, gdata
                    return True 
        return False 