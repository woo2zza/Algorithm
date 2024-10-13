

King, Stone, cnt = input().split()
King_col, King_row = int(ord(King[0])) - 64, int(King[1])
Stone_col, Stone_row = int(ord(Stone[0])) - 64, int(Stone[1])
cnt = int(cnt)

arr = ['LT', 'T', 'RT', 'L', 'R', 'LB', 'B', 'RB']
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]

for i in range(cnt):
    coor = input()
    inx = arr.index(coor)
    
    nx = King_col + dx[inx]
    ny = King_row + dy[inx]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    if nx == Stone_col and ny == Stone_row:
        n_stone_col = Stone_col + dx[inx]
        n_stone_row = Stone_row + dy[inx]

        if n_stone_col < 1 or n_stone_row < 1 or n_stone_col > 8 or n_stone_row > 8:
            continue
        
        Stone_col, Stone_row = n_stone_col, n_stone_row

    King_col, King_row = nx, ny

print(f'{chr(King_col + 64)}{King_row}')
print(f'{chr(Stone_col + 64)}{Stone_row}')
