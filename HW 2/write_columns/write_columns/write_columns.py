def write_columns(data, fname):
    '''Write input data into three columns of a comma-separated file'''
    assert isinstance(data, list) , 'input data must be a list'
    assert isinstance(fname, str), 'input filename must be a string'
    assert len(fname) > 0, 'input must not be an empty string'
    assert fname.endswith('.csv'), 'input must be a csv file name'
    assert len(data) > 0, 'input data must not be empty'
    all_data = [0]*3*len(data)
    data_value = data
    data_value2 = [d**2 for d in data_value] 
    data_value3 = [round((d+d**2)/3, 2) for d in data_value] 
    count = 0
    count2 = 1
    for a,b in zip(data_value, data_value2):
        all_data[count] = str(a) + ','
        all_data[count2] = str(b) + ','
        count += 3
        count2 += 3
    count3 = 2
    for s in range(0, len(data_value3)):
        all_data[count3] = str(data_value3[s]) + '\n'
        count3 += 3
    all_data = ''.join(all_data)
    f = open(fname, 'w')
    f.write(all_data)
    f.close()
