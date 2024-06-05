def achar_prox_vazio(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def e_valido(puzzle, guess, row, col):
    if guess in puzzle[row]:
        return False

    # Verifica se o número já está na coluna
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def resolver_sudoku(puzzle):
    row, col = achar_prox_vazio(puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if e_valido(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if resolver_sudoku(puzzle):
                return True

        puzzle[row][col] = -1

    return False

if __name__ == '__main__':
    example_board = [
        [9, 2, -1,  -1, 1, -1,  3, -1, -1],
        [8, 5, -1,  -1, 9, -1,  -1, 2, -1],
        [-1, -1, 3,  -1, -1, -1,  -1, -1, -1],

        [-1, -1, -1,  -1, -1, 2,  -1, -1, -1],
        [3, -1, -1,  -1, -1, 1,  6, -1, -1],
        [1, 9, 7,  -1, -1, -1,  2, 5, -1],

        [-1, -1, -1,  5, -1, 9,  -1, 6, 2],
        [-1, 8, 5,  -1, 2, -1,  4, -1, -1],
        [-1, -1, 9,  7, 4, -1,  -1, 3, -1],
    ]

    if resolver_sudoku(example_board):
        print("Sudoku resolvido com sucesso!")
    else:
        print("Não foi possível resolver o Sudoku.")
    print(example_board)