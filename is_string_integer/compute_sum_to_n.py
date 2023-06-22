def compute_sum_to_n(n):
    '''Computes the sum of all non-negative integers up to and including n'''
    assert isinstance(n, int), 'n must be an integer'
    assert n>=0, 'n must be a positive value'
    return sum(range(0, n+1))
