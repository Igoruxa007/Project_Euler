def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


def sudoku(puzzle):
    if solveSudoku(puzzle, 0, 0):
        return puzzle
    else:
        return False


def sudoku1(P):
    for row, col in [(r, c) for r in range(9) for c in range(9) if not P[r][c]]:

        rr, cc = (row // 3) * 3, (col // 3) * 3

        use = {1, 2, 3, 4, 5, 6, 7, 8, 9} - (
                    {P[row][c] for c in range(9)} | {P[r][col] for r in range(9)} | {P[rr + r][cc + c] for r in range(3)
                                                                                     for c in range(3)})

        if len(use) == 1:
            P[row][col] = use.pop()
            return sudoku1(P)
    return P

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


def test():
    for row, col in [(r, c) for r in range(9) for c in range(9) if not puzzle[r][c]]:
        pass


print(not puzzle[0][0])
