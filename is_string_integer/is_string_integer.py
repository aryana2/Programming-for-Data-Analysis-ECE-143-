def is_string_integer(s):
    '''After checking if input is a single string character, 
    returns whether input string character is an integer'''
    assert isinstance(s, str), 'input should be type string'
    assert len(s) == 1, 'input should be single character'
    return s.isnumeric()