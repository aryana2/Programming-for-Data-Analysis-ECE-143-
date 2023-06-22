import networkx as nx
  
def get_all_paths(source, destination):
    '''Return all possible paths from source to destination'''
    assert isinstance(source, int)
    assert isinstance(destination, int)
    assert source >= 1 and source <= 9
    assert destination >= 1 and destination <= 9
    g = nx.Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(3, 2)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    g.add_edge(4, 1)
    g.add_edge(4, 2)
    g.add_edge(4, 5)
    g.add_edge(4, 7)
    g.add_edge(4, 8)
    g.add_edge(5, 1)
    g.add_edge(5, 2)
    g.add_edge(5, 3)
    g.add_edge(5, 4)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(5, 8)
    g.add_edge(5, 9)
    g.add_edge(6, 2)
    g.add_edge(6, 3)
    g.add_edge(6, 5)
    g.add_edge(6, 8)
    g.add_edge(6, 9)
    g.add_edge(7, 4)
    g.add_edge(7, 5)
    g.add_edge(7, 8)
    g.add_edge(8, 4)
    g.add_edge(8, 5)
    g.add_edge(8, 6)
    g.add_edge(8, 7)
    g.add_edge(8, 9)
    g.add_edge(9, 5)
    g.add_edge(9, 6)
    g.add_edge(9, 8)

    paths = nx.all_simple_paths(g, source=source, target=destination)

    return paths

def get_estimated_completion_prob(x):
    '''Retrieve probabilities for a given partial sequence to end on a given value'''
    assert isinstance(x, list)
    assert all([isinstance(i, int) for i in x])
    assert all([i>=1 and i<=9 for i in x])
    assert len(x) <=9
    assert len(x) >= 1
    all_endpoints = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    endpoints = [l for l in all_endpoints if l not in x]
    filtered_paths = []
    num = []
    total = 0
    probs = {}
    for point in endpoints:
        all_paths = get_all_paths(x[-1], point)
        filtered_paths = ([i for i in all_paths if not any(j in i for j in x[:-1])])
        total += len(filtered_paths)
        num.append(len(filtered_paths))
    count = 0
    for n in endpoints:
        probs[n] = num[count]/total
        count+=1
    return probs