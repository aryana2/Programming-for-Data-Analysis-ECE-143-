def convert_hex_to_RGB(codes):
    '''Convert a list of color hex codes to a list of RGB tuples'''
    assert isinstance(codes, list), 'input must be a list'
    assert len(codes) > 0, 'input must not be empty'
    rgb = []
    for value in codes:
        assert isinstance(value, str), 'list must contain only strings'
        h = value.lstrip('#')
        rgb.append(tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

    return rgb
