import pandas as pd 
from datetime import datetime
def fix_categorical(x):
    '''Convert month-yr column dtype to Pandas CategoricalDtype with correct order'''
    assert isinstance(x, pd.DataFrame)
    assert not x.empty
    assert not x['month-yr'].empty
    timestamp = x['month-yr']
    assert all([isinstance(s, str) for s in timestamp])
    all_dates = x.drop_duplicates(subset='month-yr')['month-yr'].to_frame()
    dateList = list(x['month-yr'].unique())
    dateList.sort(key=lambda date: datetime.strptime(date, '%b-%Y'))
    s = pd.CategoricalDtype(categories=dateList, ordered=True)
    all_dates['month-yr'] = all_dates['month-yr'].astype(s)
    df = pd.DataFrame()
    df['month-yr'] = all_dates['month-yr']
    x['month-yr'] = x['month-yr'].astype(s)
    df_count = x.groupby('month-yr')['Timestamp'].count().to_frame()
    df_count = df_count.reset_index(drop=True)
    df = df.reset_index(drop=True)
    df = pd.concat([df, df_count['Timestamp']], axis=1)
    return df

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
    df_new = df_new.reset_index()
    x = pd.concat([x, df_new], axis=1)
    return x