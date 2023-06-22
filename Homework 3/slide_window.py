def slide_window(x, width, increment):
    '''Compute a sequence of overlapping lists from input list'''
    assert isinstance(x, list), 'input must be a list'
    assert len(x) > 0, 'input must not be an empty list'
    assert isinstance(x[0], int), 'input must be one-dimensional'
    assert isinstance(width, int), 'input must be an integer'
    assert isinstance(increment, int), 'input must be an integer'
    assert width > 0, 'width must be greater than 0'
    assert increment > 0, 'width must be greater than 0'
    seq = []
    seq.append(x[0:width])
    endelement = seq[-1][-1]
    check = x[-1]
    count = 0
    while endelement+increment <= check:
        new_list = [increment + seq[count][i] for i in range(len(seq[count]))]
        seq.append(new_list)
        endelement = seq[-1][-1]
        count += 1
    return seq
