def solve_queens(n=8):
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            return [[]]
        solutions = []
        for col in range(n):
            if col not in cols and row + col not in diag1 and row - col not in diag2:
                for sol in backtrack(row + 1, cols | {col}, diag1 | {row + col}, diag2 | {row - col}):
                    solutions.append([col] + sol)
        return solutions

    return backtrack(0, set(), set(), set())

def print_solution(solution):
    for row in solution:
        line = ['.'] * len(solution)
        line[row] = 'Q'
        print(' '.join(line))

solutions = solve_queens()
for solution in solutions:
    print_solution(solution)
    print()
