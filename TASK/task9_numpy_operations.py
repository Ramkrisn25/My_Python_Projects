# task9_numpy_operations.py

import numpy as np # type: ignore

def numpy_operations_demonstration():
    print("--- NumPy Array Operations ---")

    # 1. Array Creation
    arr1d = np.array([1, 2, 3, 4, 5])
    print(f"\n1D Array: {arr1d}")
    arr2d = np.array([[10, 20, 30],[40, 50, 60]])
    print(f"2D Array:\n{arr2d}\nShape: {arr2d.shape}")

    # 2. Arithmetic Operations
    arr_a = np.array([1, 2, 3])
    arr_b = np.array([4, 5, 6])
    print(f"\nArray A: {arr_a}, Array B: {arr_b}")
    print(f"A + B: {arr_a + arr_b}")
    print(f"A * 2: {arr_a * 2}")

    # 3. Aggregation Operations
    data_array = np.array([5, 8, 2, 10, 3, 7])
    print(f"\nData Array: {data_array}")
    print(f"Sum: {data_array.sum()}")
    print(f"Mean: {data_array.mean()}")
    print(f"Max: {data_array.max()}")
    print(f"Min: {data_array.min()}")

    # 4. Indexing and Slicing
    print(f"\nOriginal 1D Array: {arr1d}")
    print(f"First element: {arr1d[0]}")
    print(f"Elements 1 to 3: {arr1d[1:4]}")

    print(f"\nOriginal 2D Array:\n{arr2d}")
    print(f"Element [0, 1]: {arr2d[0, 1]}")
    print(f"First row: {arr2d[0, :]}")
    print(f"Second column: {arr2d[:, 1]}")

    print("\n--- Demo Complete ---")

if __name__ == "__main__":
    numpy_operations_demonstration()