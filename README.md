# Simplex Method Python Implementation

## Overview

This project is a Python implementation of the Simplex Method, a popular algorithm for numerical solution of Linear Programming problems. The Simplex Method is used for optimizing a linear objective function, subject to linear equality and linear inequality constraints.

## Requirements

- Python 3.x

## Usage

### Define the Linear Programming Problem

The Linear Programming Problem should be of the form:

```
Maximize c^T * x
subject to:
Ax <= b
x >= 0
```

Where:
- `c` is the coefficients of the objective function.
- `A` is the coefficients matrix of the constraints.
- `b` is the right-hand side of the constraints.
- `x` is the vector of variables to be determined.

### How to Run

1. Define the Linear Programming Problem in the main section of the script, `c`, `A`, and `b`.
2. Run the Python script using the Python interpreter.

   ```sh
   python simplex_method.py
   ```

## Example

Below is a simple example problem:

```python
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
```

## Features

- The program handles the tabulation of the Simplex Method, iteratively printing the tableau at each step.
- Displays the Basic and Non-Basic variables in every iteration.
- Shows the final optimal solution and the optimal value of the objective function.
- The program displays a well-formatted tableau at each iteration, allowing users to trace the steps of the algorithm.

## Limitations

- The implementation currently handles maximization problems only.
- The implementation assumes the feasibility of the linear programming problem, and it does not handle infeasible solutions or unbounded solutions.

## License

Distributed under the MIT License. See `LICENSE` for more information.
