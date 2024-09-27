def bomberMan(n, grid):
    if n == 1 or n == 0:
        return grid

    # If the time is even, the whole grid is full of bombs
    if n % 2 == 0:
        return [row.replace('.', 'O') for row in grid]

    # We need to simulate only for the 3rd and 4th seconds since the pattern repeats every 4 seconds
    # First, simulate the full bomb layout
    full_bombs = [row.replace('.', 'O') for row in grid]
    def explode(grid):
        result = [list(row) for row in full_bombs]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'O':
                    result[i][j] = '.'
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                            result[ni][nj] = '.'
        return [''.join(row) for row in result]
    
    # Exploding bombs placed initially
    third_second = explode(grid)
    
    # Bombs placed at third second exploding
    fourth_second = explode(third_second)
    
    # Return based on pattern repetition
    return third_second if n % 4 == 3 else fourth_second

grid = [
    '..O..',
    '.....',
    '.....'
]
for n in range(0,12):
    print(f'time: {n} seconds')
    print(bomberMan(n,grid))
    print('')

