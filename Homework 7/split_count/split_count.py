import pandas as pd
def split_count(x):
    '''Take input panda Series column and output count of categorical variables in panda dataframe'''
    assert isinstance(x, pd.Series)
    assert not x.empty
    assert x.name == 'Is there anything in particular you want to use Python for?'
    assert all([isinstance(s, str) for s in x])
    df = pd.DataFrame(columns=['count'])
    for i in range(0, len(x)):
        str_ans = x[i]
        idxs = [j for j,char in enumerate(str_ans) if char == ',']
        idxs.append(len(str_ans))
        count = 0
        for element in idxs:
            p = str_ans[count:element]
            if (df.index == p).any():
                df.loc[p] += 1
            else:
                df.loc[p] = 1
            count = element + 2
    df.sort_values(by=['count'], ascending=True)
    return df

