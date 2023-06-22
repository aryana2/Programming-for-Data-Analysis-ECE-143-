import pandas as pd 
from datetime import datetime
def add_month_yr(x):
    '''Output new month-yr column from input survey dataframe'''
    assert isinstance(x, pd.DataFrame)
    assert not x.empty
    assert not x['Timestamp'].empty
    assert isinstance(x['Timestamp'], pd.Series)
    timestamp = x['Timestamp']
    assert all([isinstance(s, str) for s in timestamp])
    assert not x['ID'].empty
    assert isinstance(x['ID'], pd.Series)
    id_var = x['ID']
    assert all([isinstance(s, int) for s in id_var])
    df = x[['Timestamp', 'ID']]
    df_new = pd.DataFrame(columns=['month-yr'])
    for i in range(0, len(df)):
        time = datetime.strptime(df.loc[i]["Timestamp"], '%m/%d/%Y %H:%M')
        s1 = pd.DataFrame([datetime.strftime(time, '%b-%Y')], index=[df.loc[i]["ID"]], columns=['month-yr'])
        df_new = pd.concat([df_new, s1])
    print(df_new)
    df_new = df_new.reset_index()
    x = pd.concat([x, df_new], axis=1)
    return x
