def fibonacci(n):
    '''Compute first n Fibonacci numbers'''
    assert isinstance(n, int), 'input must be an integer'
    assert n>=0, 'input must be at least 1'
    F = [0]*n
    for i in range(0, n):
        if i == 0:
            F[0] = 1
        elif i == 1:
            F[1] = 1
        else:
            F[i] = F[i-1] + F[i-2]
        yield F[i]
