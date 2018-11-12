import numpy as np


def inverse_tensor(A):
    delta_inv = .5 / (A[0] * A[5] - A[2] * A[3])
    Ai = np.zeros(6)
    Ai[0] = .5 * A[5] * delta_inv
    Ai[1] = 1 / A[1]
    Ai[2] = -A[5] * delta_inv
    Ai[3] = Ai[2]
    Ai[4] = 4 / A[4]
    Ai[5] = 2 * A[0] * delta_inv
    return Ai


def multiply(A, B):
    Ai = np.zeros(6)
    Ai[0] = A[0] * B[0] * 2 + A[2] * B[3]
    Ai[1] = A[1] * B[1]
    Ai[2] = A[0] * B[2] * 2 + A[2] * B[5]
    Ai[3] = A[3] * B[0] * 2 + A[5] * B[3]
    Ai[4] = A[4] * B[4] * .5
    Ai[5] = A[3] * B[2] * 2 + A[5] * B[5]
    return Ai
