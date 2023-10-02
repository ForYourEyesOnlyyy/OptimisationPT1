def print_tableau(table):
    """
    Function to print the tableau in a readable format.
    """
    for row in table:
        print(' | '.join(f"{val:.2f}" for val in row))
    print('-' * 40)


def simplex(c, A, b):
    m, n = len(A), len(c)
    table = [row + [0] * m + [b[idx]] for idx, row in enumerate(A)]

    for i in range(m):
        table[i][n + i] = 1

    table.append([i * -1 for i in c] + [0] * m + [0])

    iteration = 1
    while any(value < 0 for value in table[-1][:-1]):
        print(f"Iteration {iteration}")
        print_tableau(table)

        pivot_col_idx = table[-1].index(min(table[-1][:-1]))
        pivot_row_idx = None
        min_ratio = float('inf')
        for i, row in enumerate(table[:-1]):
            if row[pivot_col_idx] <= 0:
                continue
            ratio = row[-1] / row[pivot_col_idx]
            if ratio < min_ratio:
                min_ratio, pivot_row_idx = ratio, i

        if pivot_row_idx is None:
            raise ValueError("No feasible solution exists.")

        pivot(table, pivot_row_idx, pivot_col_idx)
        iteration += 1

    print("Final Tableau:")
    print_tableau(table)

    solution = [0] * n
    for row in table[:-1]:
        for i, value in enumerate(row[:-1]):
            if value == 1 and sum(row[:-1]) == 1:
                solution[i] = row[-1]

    return solution, table[-1][-1]


def pivot(table, row, col):
    pivot_val = table[row][col]
    table[row] = [element / pivot_val for element in table[row]]

    for i, current_row in enumerate(table):
        if i == row:
            continue
        multiplier = current_row[col]
        table[i] = [element - multiplier * table[row][idx] for idx, element in enumerate(current_row)]


if __name__ == '__main__':
    c = [3, 2]
    A = [
        [1, 2],
        [2, 1]
    ]
    b = [4, 3]
    solution, objective_value = simplex(c, A, b)
    print(f"Optimal Solution: {solution}")
    print(f"Optimal Value: {objective_value}")
