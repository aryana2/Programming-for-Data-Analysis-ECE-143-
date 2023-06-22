def count_paths(m, n, blocks):
    '''find the number of connected paths between the top-left square and the bottom right square 
    by traversing only the intermediate squares with the . symbol.'''
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert isinstance(blocks, list)
    assert m >= 0
    assert n >= 0
    assert all([isinstance(b, tuple) for b in blocks])
    gridpath = [[0]*n for _ in range(m)]
    for b in blocks:
        assert all([isinstance(i, int) for i in b])
        assert b!= (0,0)
        assert b!= (m-1,n-1)
        assert len(b) == 2
        gridpath[b[0]][b[1]] = 1
    
    return path_finder(0, 0, m, n, gridpath)

def path_finder(i, j, r, c, A):
    if(i == r or j == c):
      return 0
     
    if(A[i][j] == 1):
      return 0
     
    # base case
    if(i == r-1 and j == c-1):
      return 1
    
    return path_finder(i+1,j,r,c,A) + path_finder(i,j+1,r,c,A)
