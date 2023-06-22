import numpy as np
import math

def solvefrob(coefs, b):
    '''Solve the Frobenius equation'''
    assert isinstance(coefs, list)
    assert len(coefs) > 0
    assert all(isinstance(c, int) for c in coefs)
    assert all([c > 0 for c in coefs])
    assert isinstance(b, int)
    assert b > 0
    x_i = [0]*len(coefs)
    sol = []
    gcd = math.gcd(*coefs)
    if b % gcd:
        return sol
    max_ranges = []
    for c in coefs:
        div = math.floor(b/c)
        max_ranges.append(np.arange(div+1))
    cum_sum = 0
    idx = 0
    reshape_array = [len(max_ranges[idx])]
    for pos in max_ranges:
        reshape_array[0] = len(max_ranges[idx])
        cum_sum = cum_sum + np.reshape(pos, reshape_array)*coefs[idx]
        idx += 1
        reshape_array.append(1)
    true_sum = np.where(cum_sum == b)
    xr = len(true_sum)-1
    yr = len(true_sum[0])
    for i in range(0, yr):
        ans = []
        for j in range(xr, -1, -1):
            ans.append(true_sum[j][i])
        sol.append(tuple(ans))
    return sol
