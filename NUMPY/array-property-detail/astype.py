import numpy as np
arr = np.array([1.5, 2.5, 3.5, 4.5, 6.5])
print(arr.dtype)

int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)
