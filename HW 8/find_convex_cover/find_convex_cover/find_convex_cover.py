import numpy as np
from collections import defaultdict

def find_convex_cover(pvertices,clist):
    '''
    compute the radii of m circles centered at those m points such that the sum of the areas of the circles is minimized (approximately) and that any vertex in 
    P is also contained in at least one of the m circles.
    '''
    assert isinstance(pvertices, np.ndarray)
    assert all([isinstance(p, np.ndarray) for p in pvertices])
    for p in pvertices:
        assert all([isinstance(q, float) for q in p])
    assert isinstance(clist, list)
    assert all([isinstance(i, tuple) for i in clist])
    for i in clist:
        assert all([isinstance(j, float) for j in i])

    x_v = pvertices[:, 0]
    y_v = pvertices[:, 1]
    clist = np.array(clist)
    x_c = clist[:, 0]
    y_c = clist[:, 1]

    dist = np.sqrt(
        abs(x_v.reshape(-1, 1)[:, None] - x_c.reshape(-1, 1)) ** 2
        + abs(y_v.reshape(-1, 1)[:, None] - y_c.reshape(-1, 1)) ** 2)

    min_v = [
        (x, y)
        for x, y in zip(
            np.sort(dist, axis=1)[:, 0][:, 0], np.argsort(dist, axis=1)[:, 0][:, 0]
        )
    ]

    mapi = defaultdict(int)
    for d, v in min_v:
        mapi[v] = max(mapi[v], d)

    ans = [mapi[i] for i in range(len(clist))]

    return ans