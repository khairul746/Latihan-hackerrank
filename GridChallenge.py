def gridChallenge(grid):
    sorted_grid = [sorted(row) for row in grid]
    n = len(grid) # number of rows
    m = len(grid[0]) # number of columns
    cols = {}
    for i in range(m):
        col = []
        for j in range(n):
            col.append(sorted_grid[j][i])
            cols[i] = col
        if cols[i] != sorted(cols[i]):
            return 'NO'
    return 'YES'
grid = ['vpvv','pvvv','vzzp','zzyy']
print(grid)
print(gridChallenge(grid))

