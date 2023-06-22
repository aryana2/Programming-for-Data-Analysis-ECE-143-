def compute_average_word_length(instring, unique=False):
    '''Computes average length of word in given string including or excluding duplicates'''
    assert isinstance(instring, str), 'text input must be type string'
    assert isinstance(unique, bool), 'unique input must be type boolean'
    assert len(instring) > 0, 'input string must be at least one character'
    words = instring.split()
    if unique:
        res = []
        [res.append(x) for x in words if x not in res]
        words = res
    return sum(len(word) for word in words)/len(words)

s = "Mary had a little lamb\nits fleece was white as snow\nand everywhere that Mary went\nthe lamb was sure to go"
print(compute_average_word_length(s, True))
