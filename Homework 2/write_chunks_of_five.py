def write_chunks_of_five(words, fname):
    '''Create new file consisting of each consecutive non-overlapping sequence of five lines merged into one line'''
    assert isinstance(words, list), 'input must be a list'
    assert isinstance(words[0], str), 'input must be one-dimensional'
    assert all(isinstance(x, str) for x in words), 'all elements in input must be string'
    assert isinstance(fname, str), 'filename input must be string'
    assert len(fname) > 0, 'input filename must not be an empty string'
    assert fname.endswith('.txt'), 'filename must end with .txt extension'
    assert len(words) > 0, 'input list must not be empty'
    div = 5
    lines = []
    count = 0
    for i in range(0, len(words), div):
        text = words[i:i+div]
        res = []
        for sub in text:
            res.append(sub.replace('\n', ''))
        text = ' '.join(res[:-1])
        text = text + ' ' + res[-1] + '\n'
        lines.append(text)
        f = open(fname, 'a')
        f.write(lines[count])
        f.close()
        count += 1