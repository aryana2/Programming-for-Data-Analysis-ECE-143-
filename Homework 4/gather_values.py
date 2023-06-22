import itertools

def gather_values(seq):
    '''Generate a dictionary with bitstrings as keys and with values as lists containing corresponding mapped values'''
    assert isinstance(seq, list)
    assert all(isinstance(x, str) for x in seq)
    nbits = len(seq[0])
    bitstrings = ["".join(s) for s in itertools.product("01", repeat=nbits)]
    assert set(seq).issubset(set(bitstrings))
    map_dict = map_bitstring(seq)
    map_tally = {}
    l = list(set(seq))
    for s in l:
        map_tally[s] = []
    for s in seq:
        map_tally[s].append(map_dict.get(s))
    return map_tally

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
