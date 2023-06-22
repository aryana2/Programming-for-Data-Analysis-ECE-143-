import numpy as np
import itertools
import math
def get_sample(nbits=3, prob=None, n=1):
    '''Return a list n of random samples from a finite possibility mass dictionary'''
    assert isinstance(nbits, int), 'nbits input must be an integer'
    assert nbits > 0, 'nbits input must be at least 1'
    assert isinstance(prob, dict), 'prob input must be a dict'
    assert isinstance(n, int), 'n must be an integer'
    assert n > 0, 'n must be at least 1'
    bitstrings = ["".join(seq) for seq in itertools.product("01", repeat=nbits)]
    key = list(prob.keys())
    assert len(key) == len(bitstrings)
    assert set(key) == set(bitstrings)
    val = list(prob.values())
    assert(sum(val)) == 1
    sample = np.random.choice(key, n, p=val)
    return list(sample)