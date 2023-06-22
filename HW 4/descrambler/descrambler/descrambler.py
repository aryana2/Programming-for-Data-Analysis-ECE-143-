import itertools

def descrambler(w, k):
    '''Generate a phrase of k words from n lower-case letters'''
    assert isinstance(w, str)
    assert len(w) > 0
    assert isinstance(k, tuple)
    assert len(k) > 0
    assert all(isinstance(x, int) for x in k)
    assert k[-1] <= len(w)
    fname = '/tmp/google-10000-english-no-swears.txt'
    f=open(fname,'r')
    words = [i.strip("\n") for i in f.readlines()]
    k = tuple(sorted(k, reverse=True))
    count = 0
    match = find_words(w, k[count], words)
    leftover = w
    my_dict = {}
    done = True
    if match:
        if len(k) == 1:
            for m in match:
                yield m
        else:
            count += 1
            for subword in match:
                my_dict[subword] = [] 
                leftover = eliminate_letters(w, subword)
                new_match = find_words(leftover, k[count], words)
                if new_match:
                    my_dict[subword] = new_match
            if len(k) == count+1:
                for key, val in my_dict.items():
                    for subword in val:
                        concat_word = subword + " " + key
                        yield concat_word
            else:
                while done:
                    count += 1
                    new_dict = {}
                    for key, val in my_dict.items():
                        for subword in val:
                            concat_word = subword + " " + key
                            new_dict[concat_word] = []
                            leftover = eliminate_letters(w, concat_word.replace(" ", ""))
                            new_match = find_words(leftover, k[count], words)
                            if new_match:
                                new_dict[concat_word] = new_match
                    my_dict = new_dict
                    if len(k) == count+1:
                        for key, val in my_dict.items():
                            for subword in val:
                                concat_word = subword + " " + key
                                yield concat_word
                        done = False
    else:
        yield []

def find_words(w, k, words):
    matched_words = []
    len_words = [s for s in words if len(s) == k]
    for l in len_words:
        ref = w
        nope = True
        for letter in l:
            if letter in ref:
                ref = ref.replace(letter, '', 1)
            else:
                nope = False
                break
        if nope:
            matched_words.append(l)
    return list(matched_words)

def eliminate_letters(leftover, subword):
    for s in subword:
        leftover = leftover.replace(s, '', 1)
    return leftover


