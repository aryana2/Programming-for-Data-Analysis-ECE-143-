import numpy as np
import random

def gen_rand_slash(m=6, n=6, direction='back'):
    '''Produce a uniformly random forward or backslashed image'''
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert isinstance(direction, str)
    assert direction == 'back' or direction == 'forward'
    assert m>1
    assert n>1

    max_len = min(m, n)
    len_array = random.choice(range(2,max_len+1))
    array = np.zeros([m,n])
    
    if direction=='back':
        # start position
        r_pos = random.choice(range(m-len_array+1))
        c_pos = random.choice(range(n-len_array+1))
        for i in range(len_array):
            array[r_pos][c_pos] = 1
            r_pos += 1
            c_pos += 1
    else:
        # start position
        r_pos = random.choice(range(m-len_array+1))
        c_pos = random.choice(range(len_array-1,n))
        for i in range(len_array):
            array[r_pos][c_pos] = 1
            r_pos += 1
            c_pos -= 1        
    
    return array
