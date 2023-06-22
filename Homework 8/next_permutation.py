def next_permutation(t):
    '''Given a permutation of any length, generate the next permutation in lexicographic order.'''
    assert isinstance(t, tuple)
    assert len(t) > 0
    assert all([isinstance(i, int) for i in t])
    assert len(set(t)) == len(t)
    n = len(t)
    for i in range(n-2, -1, -1):
        if t[i] < t[i+1]:
            break
    if i == 0:
        arr = t[::-1]
    else:
        for j in range(n-1, i, -1):
            if t[j] > t[i]:
                break
        arr = list(t)
        arr[i], arr[j] = arr[j], arr[i]
        strt, end = i+1, len(arr)
        arr[strt:end] = arr[strt:end][::-1]
    return tuple(arr)