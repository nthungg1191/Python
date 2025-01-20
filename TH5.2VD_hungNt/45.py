import numpy as np

# Define the matrix
A = np.array([
    [3, -1, -2],
    [3, 2, -3],
    [1, 2, 0]
])

# Compute the trace
trace_A = np.trace(A)

print(f"The trace of the matrix A is: {trace_A}")
