def get_average_word_length(words):
    '''Compute average length of words'''
    assert isinstance(words, list)
    assert all(isinstance(w, str) for w in words)
    assert all(len(w) > 0 for w in words)
    len_words = [len(s) for s in words]
    return sum(len_words) / len(len_words)

def get_longest_word(words):
    '''Determine longest word'''
    assert isinstance(words, list)
    assert all(isinstance(w, str) for w in words)
    assert all(len(w) > 0 for w in words)
    len_words = [len(s) for s in words]
    return words[len_words.index(max(len_words))]

def get_longest_words_startswith(words, start):
    '''Determine longest word that starts with a given character'''
    assert isinstance(words, list)
    assert all(isinstance(w, str) for w in words)
    assert all(len(w) > 0 for w in words)
    assert isinstance(start, str)
    assert len(start) == 1
    assert start.isalpha()
    words = [s for s in words if s[0] == start]
    len_words = [len(s) for s in words]
    return words[len_words.index(max(len_words))]

def get_most_common_start(words):
    '''Determine most common starting letter'''
    assert isinstance(words, list)
    assert all(isinstance(w, str) for w in words)
    assert all(len(w) > 0 for w in words)
    words_firstletter = [s[0] for s in words]
    return max(set(words_firstletter), key=words_firstletter.count)

def get_most_common_end(words):
    '''Determine most common ending letter'''
    assert isinstance(words, list)
    assert all(isinstance(w, str) for w in words)
    assert all(len(w) > 0 for w in words)
    words_lastletter = [s[-1] for s in words]
    return max(set(words_lastletter), key=words_lastletter.count)