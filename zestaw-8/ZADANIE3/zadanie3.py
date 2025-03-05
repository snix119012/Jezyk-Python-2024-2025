import numpy as np
import time
from numba import jit, prange, vectorize

# Python List implementacja
def sum_of_squares_list(data):
    result = 0
    for x in data:
        result += x**2
    return result

# NumPy Array implementacja
def sum_of_squares_numpy(data):
    return np.sum(data**2)

# Numba implementacja
@jit(nopython=True)
def sum_of_squares_numba(data):
    result = 0
    for x in data:
        result += x**2
    return result

@jit(nopython=True, fastmath=True)
def sum_of_squares_numba_fastmath(data):
    result = 0
    for x in data:
        result += x**2
    return result

@jit(nopython=True, parallel=True)
def sum_of_squares_numba_parallel(data):
    result = 0
    for i in prange(len(data)):
        result += data[i]**2
    return result

@vectorize(['int64(int64)'], target='parallel')
def square(x):
    return x**2

if __name__ == "__main__":
    n = 300_000
    data_list = [i for i in range(n)]
    data_numpy = np.array(data_list, dtype=np.int64)

    start_time = time.time()
    result_list = sum_of_squares_list(data_list)
    end_time = time.time()
    print(f"Python List: {result_list}, Time: {end_time - start_time:.6f}s")

    start_time = time.time()
    result_numpy = sum_of_squares_numpy(data_numpy)
    end_time = time.time()
    print(f"NumPy Array: {result_numpy}, Time: {end_time - start_time:.6f}s")

    start_time = time.time()
    result_numba_list = sum_of_squares_numba(data_list)
    end_time = time.time()
    print(f"Numba (List): {result_numba_list}, Time: {end_time - start_time:.6f}s")

    start_time = time.time()
    result_numba_list = sum_of_squares_numba(data_list)
    end_time = time.time()
    print(f"Numba (List, second call): {result_numba_list}, Time: {end_time - start_time:.6f}s")

    start_time = time.time()
    result_numba_array = sum_of_squares_numba(data_numpy)
    end_time = time.time()
    print(f"Numba (Array): {result_numba_array}, Time: {end_time - start_time:.6f}s")

    start_time = time.time()
    result_numba_fastmath = sum_of_squares_numba_fastmath(data_numpy)
    end_time = time.time()
    print(f"Numba (FastMath): {result_numba_fastmath}, Time: {end_time - start_time:.6f}s")

    start_time = time.time()
    result_numba_parallel = sum_of_squares_numba_parallel(data_numpy)
    end_time = time.time()
    print(f"Numba (Parallel): {result_numba_parallel}, Time: {end_time - start_time:.6f}s")

    start_time = time.time()
    result_vectorized = np.sum(square(data_numpy))
    end_time = time.time()
    print(f"Numba (Vectorized): {result_vectorized}, Time: {end_time - start_time:.6f}s")
