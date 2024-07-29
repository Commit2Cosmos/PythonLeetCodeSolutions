# measure.py
import time

import funcs_rs
from n_queens_py import sol


solve_queen_rs = funcs_rs.solve_n_queens
solve_queen_py = sol.solveNQueens


NUM_ITER = 20
N = 10

def ttr(func):
    t0 = time.perf_counter()

    for _ in range(NUM_ITER):
        func(N)

    t1 = time.perf_counter()

    took = (t1 - t0) / NUM_ITER
    print(f"Took and avg of {took*10e3:.2f} ms per iteration")


ttr(solve_queen_rs)
ttr(solve_queen_py)