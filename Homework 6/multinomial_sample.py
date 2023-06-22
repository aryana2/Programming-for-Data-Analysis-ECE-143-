import random
def multinomial_sample(n, p, k=1):
    '''                                                                 
    Return samples from a multinomial distribution.                     
                                                                             
    n:= number of trials                                                
    p:= list of probabilities                                           
    k:= number of desired samples                                       
    '''
    assert isinstance(n, int)
    assert n>0
    assert isinstance(p, list)
    assert len(p) > 0
    assert all([num >= 0 and num <=1 for num in p])
    assert sum(p) == 1
    assert isinstance(k, int)
    assert k > 0
    all_outcomes = []
    choices = range(0, len(p))
    weights = [chances*(1/min(p)) for chances in p]
    for i in range(0, k):
        outcomes = [0]*len(p)
        for j in range(0, n):
            prob = random.choices(choices, weights)[0]
            outcomes[prob] += 1
        all_outcomes.append(outcomes)
    return all_outcomes