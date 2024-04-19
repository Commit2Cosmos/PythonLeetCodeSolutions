import numpy as np


n = 100
G = 20
x = 5


everything = np.zeros((n), dtype=np.int64)

everything[:x] = 1


np.random.shuffle(everything)

total = 100000

#! Without replacement
counter = 0

for _ in range(total):
    chosen = np.random.choice(everything, G, replace=False)
    if np.any(chosen == 1):
        counter += 1

print(f"probability to encounter at least 1 '1' without replacement {counter/total}")


#! With replacement
counter = 0

for _ in range(total):
    chosen = np.random.choice(everything, G, replace=True)
    if np.any(chosen == 1):
        counter += 1

print(f"probability to encounter at least 1 '1' with replacement {counter/total}")