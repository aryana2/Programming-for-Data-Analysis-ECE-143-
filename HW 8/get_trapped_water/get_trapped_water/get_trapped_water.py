def get_trapped_water(seq):
    '''Compute how many units of water remain trapped between the walls in the map.'''
    assert isinstance(seq, list)
    assert len(seq) > 0
    assert all([isinstance(i, int) for i in seq])
    assert all([i>=0 for i in seq])

    stack = []
    n = len(seq)
    ans = 0
    for i in range(n):
        while(len(stack)!=0 and (seq[stack[-1]] < seq[i])):
            pop_height = seq[stack[-1]]
            stack.pop()
            if (len(stack) == 0):
                break
            dis = i - stack[-1] - 1
            min_height = min(seq[stack[-1]], seq[i])-pop_height
            ans += dis * min_height
        stack.append(i)
    return ans