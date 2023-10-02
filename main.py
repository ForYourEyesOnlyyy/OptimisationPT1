def print_tableau(table, header_variables, basic_variables):
    """
    Function to print the tableau in a readable format.
    """
    header = ["BV"] + header_variables + ["Solution", "Ratio"]
    row_format = "{:<12}" * (len(header))
    print(row_format.format(*header))
    print('-' * len(header) * 12)

    pivot_col_idx = None
    if any(value < 0 for value in table[-1][:-1]):
        pivot_col_idx = table[-1].index(min(table[-1][:-1]))

    for idx, row in enumerate(table[:-1]):
        ratio = "{:.2f}".format(row[-1] / row[pivot_col_idx]) if pivot_col_idx is not None and row[
            pivot_col_idx] > 0 else "∞"
        print(row_format.format(basic_variables[idx], *["{:.2f}".format(val) for val in row], ratio))
    print(row_format.format("Objective", *["{:.2f}".format(val) for val in table[-1]], "∞"))
    print('=' * len(header) * 12)


def simplex(c, A, b):
    m, n = len(A), len(c)
    non_basic_variables = ["x" + str(i) for i in range(1, n + 1)] + ["s" + str(i) for i in range(1, m + 1)]
    basic_variables = ["s" + str(i) for i in range(1, m + 1)]

    header_variables = non_basic_variables.copy()

    table = [row + [0] * m + [b[idx]] for idx, row in enumerate(A)]
    for i in range(m):
        table[i][n + i] = 1

    table.append([i * -1 for i in c] + [0] * m + [0])

    iteration = 1
    while any(value < 0 for value in table[-1][:-1]):
        print(f"Iteration {iteration}")
        print_tableau(table, header_variables, basic_variables)

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

        basic_variables[pivot_row_idx], non_basic_variables[pivot_col_idx] = non_basic_variables[pivot_col_idx], \
        basic_variables[pivot_row_idx]
        pivot(table, pivot_row_idx, pivot_col_idx)
        iteration += 1

    print("Final Tableau:")
    print_tableau(table, header_variables, basic_variables)

    solution = [0] * n
    for idx, variable in enumerate(basic_variables):
        if variable[0] == 'x':
            solution[int(variable[1:]) - 1] = table[idx][-1]
    for idx, variable in enumerate(non_basic_variables):
        if variable[0] == 'x':
            solution[int(variable[1:]) - 1] = 0

    return solution, table[-1][-1]

def pivot(table, pivot_row_idx, pivot_col_idx):
    """
    Perform pivoting on the table.
    """
    pivot_element = table[pivot_row_idx][pivot_col_idx]
    table[pivot_row_idx] = [val / pivot_element for val in table[pivot_row_idx]]

    for idx, row in enumerate(table):
        if idx == pivot_row_idx:
            continue
        factor = row[pivot_col_idx]
        table[idx] = [elem - factor * table[pivot_row_idx][i] for i, elem in enumerate(row)]


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
