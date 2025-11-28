# Generador y solucionador de Sudoku en Python
# - Genera una cuadrícula completa válida (llenada) usando backtracking aleatorio.
# - Remueve números para crear un puzzle con distinta dificultad (número de pistas/clues).
# - Incluye un solucionador por backtracking para verificar/mostrar la solución.
# - Imprime el puzzle y la solución en consola.

import random
import copy
from textwrap import dedent

def print_board(board):
    """Imprime el tablero en un formato legible."""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        row_str = ""
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += (str(val) if val != 0 else ".") + " "
        print(row_str)
    print()

def find_empty(board):
    """Encuentra la primera celda vacía (valor 0). Devuelve (fila, col) o None si completo."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, num, pos):
    """Comprueba si 'num' puede colocarse en 'pos' (fila, col) sin violar reglas del Sudoku."""
    r, c = pos
    # fila
    if any(board[r][j] == num for j in range(9) if j != c):
        return False
    # columna
    if any(board[i][c] == num for i in range(9) if i != r):
        return False
    # subcuadrícula 3x3
    start_r, start_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(start_r, start_r + 3):
        for j in range(start_c, start_c + 3):
            if (i, j) != pos and board[i][j] == num:
                return False
    return True

def solve(board):
    """Resuelve el Sudoku por backtracking. Modifica 'board' y devuelve True si se resuelve."""
    empty = find_empty(board)
    if not empty:
        return True  # completado
    r, c = empty
    for num in range(1, 10):
        if is_valid(board, num, (r, c)):
            board[r][c] = num
            if solve(board):
                return True
            board[r][c] = 0
    return False

def generate_full_board():
    """Genera un tablero completo válido mediante backtracking y relleno aleatorio de números."""
    board = [[0]*9 for _ in range(9)]
    # Rellenar diagonal 3x3 para ayudar a la aleatoriedad y acelerar
    for k in range(3):
        start_r, start_c = 3*k, 3*k
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                board[start_r + i][start_c + j] = nums.pop()
    # Usar el solucionador para completar con un orden aleatorio de números
    def solve_random(b):
        empty = find_empty(b)
        if not empty:
            return True
        r, c = empty
        nums = list(range(1, 10))
        random.shuffle(nums)
        for num in nums:
            if is_valid(b, num, (r, c)):
                b[r][c] = num
                if solve_random(b):
                    return True
                b[r][c] = 0
        return False
    solve_random(board)
    return board

def remove_numbers(board, clues=36):
    """Elimina números para crear un puzzle con exactamente 'clues' pistas (aprox)."""
    # 'clues' = número de celdas no vacías que queremos dejar.
    assert 17 <= clues <= 81, "El sudoku válido necesita al menos 17 pistas si quieres una única solución (aprox)."
    puzzle = copy.deepcopy(board)
    # Lista de posiciones posibles para borrar
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    to_remove = 81 - clues
    removed = 0

    for (r, c) in positions:
        if removed >= to_remove:
            break
        # Guardamos el valor y borramos temporalmente
        backup = puzzle[r][c]
        puzzle[r][c] = 0

        # Para acelerar, no comprobamos unicidad de solución exhaustiva (costoso).
        # En cambio, comprobamos si hay al menos UNA solución: si no, revertimos.
        test_board = copy.deepcopy(puzzle)
        if not solve(test_board):
            # quitar este número hace el puzzle insolvable -> revertir
            puzzle[r][c] = backup
        else:
            removed += 1

    return puzzle

def generate_sudoku(difficulty='medium'):
    """Genera un puzzle. difficulty en {'easy','medium','hard'}."""
    if difficulty == 'easy':
        clues = 40  # más pistas
    elif difficulty == 'hard':
        clues = 28  # menos pistas
    else:
        clues = 34  # medium por defecto
    full = generate_full_board()
    puzzle = remove_numbers(full, clues=clues)
    return puzzle, full

# --- Ejecución de ejemplo ---
if __name__ == "__main__":
    random.seed()  # semilla aleatoria
    difficulty = 'medium'  # prueba con 'easy', 'medium' o 'hard'
    puzzle, solution = generate_sudoku(difficulty=difficulty)

    print(dedent(f"""\
    Sudoku generado (dificultad: {difficulty})
    Pistas visibles ('.' = celda vacía):
    """))
    print_board(puzzle)

    print("Solución:")
    print_board(solution)
