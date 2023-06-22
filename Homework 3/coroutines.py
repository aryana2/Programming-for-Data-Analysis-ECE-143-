from types import GeneratorType

def tracker(p, limit):
    '''Count number of times odd numbered seconds that have been iterated over'''
    assert isinstance(p, GeneratorType), "input producer must be generator type"
    assert isinstance(limit, int), 'limit must be an integer'
    assert limit > 0, 'limit must be at least 1'
    count = 0
    while True:
        secs = next(p).seconds
        lim = (yield count)
        if lim != None:
            assert isinstance(lim, int), 'new limit must be an integer'
            assert lim > 0, 'new limit must be at least 1'
            if lim < count:
                yield []
                break
            limit = lim
        if secs == 0:
            count = 0
        elif secs % 2 != 0:
            count += 1
            if count > limit:
                break
