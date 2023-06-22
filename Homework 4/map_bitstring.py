import itertools
def map_bitstring(x):
    '''Maps each bitstring in x to 0 if number of 0s exceeds number of 1s'''
    assert isinstance(x, list)
    assert all(isinstance(s, str) for s in x)
    nbits = len(x[0])
    bitstrings = ["".join(seq) for seq in itertools.product("01", repeat=nbits)]
    
    assert set(x).issubset(set(bitstrings))
    
    instr = list(set(x))
    
    map_dict = {}
    for s in instr:
        if s.count('0')>s.count('1'):
            map_dict[s] = 0
        else:
            map_dict[s] = 1
    
    return map_dict
