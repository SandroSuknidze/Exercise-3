def bomber(grid, r, c):
    f_grid = [['O' for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                f_grid[i][j] = '.'
                if i+1 < r:
                    f_grid[i+1][j] = '.'
                if i > 0:
                    f_grid[i-1][j] = '.'
                if j+1 < c:
                    f_grid[i][j+1] = '.'
                if j > 0:
                    f_grid[i][j-1] = '.'
    return f_grid


r, c, n = map(int, input().split())
grid = []
for i in range(r):
    row = list(input())
    grid.append(row)

if n % 2 == 0:
    f = [''.join(['O' for i in range(c)]) for j in range(r)]
    print('\n'.join(f))
else:
    bomb1 = bomber(grid, r, c)
    bomb2 = bomber(bomb1, r, c)

    if n == 1:
        for i in range(r):
            print(''.join(grid[i]))
    elif (n + 1) % 4 == 0:
        for i in range(r):
            print(''.join(bomb1[i]))
    else:
        for i in range(r):
            print(''.join(bomb2[i]))