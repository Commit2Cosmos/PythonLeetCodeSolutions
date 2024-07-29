# measure.py
import time



t0 = time.perf_counter()

for _ in range(NUM_ITER):
    pass

t1 = time.perf_counter()

took = (t1 - t0) / NUM_ITER
print(f"Took and avg of {took*10e6} micro secs per iteration")