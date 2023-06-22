import itertools

def get_power_of3(val):
    '''Construct a number between 1 and 40 from given set 
    using addition and subtraction operations without re-using elements'''
    assert isinstance(val, int), 'input must be an integer'
    assert val > 0, 'input must be between 1 and 40'
    assert val < 41, 'input must be between 1 and 40'
    weights = [1,3,9,27]    
    coeff = [0]*len(weights)
    if val in weights:
        coeff[weights.index(val)] = 1
        return coeff
    alt = 1
    running_val = val
    while running_val > 0:
        sums = list(itertools.takewhile(lambda x: x<=running_val, itertools.accumulate(weights)))
        if sums[-1] < running_val:
            idx = weights.index(weights[len(sums)])
            coeff[idx] = 1*alt
            total = sum([a*b for a,b in zip(weights, coeff)])
            if total < val:
                alt = 1
            elif total > val:
                alt = -1
            running_val = abs(weights[len(sums)] - running_val)
        elif sums[-1] == running_val:
            total = sum([a*b for a,b in zip(weights, coeff)])
            if total > val:
                coeff[:len(sums)] = [-1]*len(sums)
            elif total < val:
                coeff[:len(sums)] = [1]*len(sums)
            else:
                coeff[:len(sums)] = [0]*len(sums)
            return coeff
    return coeff