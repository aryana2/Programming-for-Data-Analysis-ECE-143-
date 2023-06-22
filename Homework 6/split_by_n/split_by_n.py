import math
def split_by_n(fname,n=3):
    '''
    A fuction split a file into n chuncks. The end of each chunck has a complete line. 
    :param: fname (input file name)
    :type : str
    :param: n (# of chunks splitted into)
    :type : int
    '''
    assert isinstance(n,int)
    assert isinstance(fname,str)
    assert fname[-4:] == '.txt'
    assert n>=1
    
    lines=[]
    lengths=[]

    with open(fname) as f:
        for line in f:
            lines.append(line)
            lengths.append(len(line))

    cumlengths = [lengths[0]]
    for i in range(1, len(lengths)):
        cumlengths.append(cumlengths[i-1] + lengths[i])
    totalsize = sum(lengths)
    chunksize = math.ceil(totalsize/n)
    starts = [0]
    count = chunksize
    for i in range(0, n):
        starts.append([x[0] for x in enumerate(cumlengths) if x[1] <= count][-1]+1)
        count += chunksize

    for k in range(n):
        if k < 10:
            str_add = '00' + str(k)
        elif k >= 10 and k < 100:
            str_add = '0' + str(k)
        else:
            str_add = str(k)
        with open(fname+ '_' + str_add + '.txt','w') as f:
            s=slice(starts[k],starts[k+1])
            f.writelines(lines[s])   
    return